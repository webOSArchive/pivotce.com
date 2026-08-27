# Deploying the pivotCE archive

Static Hugo site served from **`www.webosarchive.org/pivot/`**, with
[Sveltia CMS](https://sveltiacms.app) at `/pivot/admin/`. The archive is built
from a git clone on the server and published into the existing www docroot, so
the web server gains no new application: it is serving files, plus one 15-line
PHP proxy and a small OAuth relay.

Living under www rather than on its own host removes work:

- `/pivot/menu.php` is handled by the PHP already configured for the site — no
  new FPM pool, no new vhost.
- TLS, http fallback for legacy webOS devices, and Matomo all come from the
  existing server config.
- `wosa-menu.js` needs no change: it derives its root from its own script URL,
  so at `/pivot/js/wosa-menu.js` it fetches `/pivot/menu.php`.

`pivot.webosarchive.org` and `pivotce.webosarchive.org` redirect here.

## 1. Getting the site onto the server

Only the **build output** is served. Never point the docroot at a clone of this
repo: that would put `raw/`, the conversion scripts and a large `.git` under the
web root, and the servable site is `public/`, not the repo root.

The repo is public, so the server can pull and build it itself — no CI, no
deploy keys, no credentials anywhere.

**One-time setup**

**Hugo 0.146 or newer is required.** Do not use `apt install hugo`: Ubuntu
22.04 ships 0.92, which predates `hugo.toml` and fails with *"Unable to locate
config file"*. Worse, anything below 0.146 does not read the render hooks in
`layouts/_markup/` — it builds without complaint while emitting every
in-article link and image without the `/pivot` prefix, so all of them point
outside the subdirectory. `deploy.sh` checks the version and refuses to run
rather than publish that.

```sh
sudo apt remove hugo                       # if a packaged one is installed
curl -fsSLO https://github.com/gohugoio/hugo/releases/download/v0.165.0/hugo_extended_0.165.0_linux-amd64.deb
sudo dpkg -i hugo_extended_0.165.0_linux-amd64.deb
hugo version
which hugo                                 # usually /usr/local/bin/hugo

git clone --depth 1 https://github.com/webOSArchive/pivotce.com /home/wosa/pivotce-src
mkdir -p /home/wosa/wosa-web/pivot
```

The `.deb` installs to `/usr/local/bin`, not `/usr/bin`, so if you removed a
packaged Hugo first your shell may still report `bash: /usr/bin/hugo: No such
file or directory` — that is bash's cached command path, cleared with `hash -r`.
`deploy.sh` looks in both directories and then `PATH`, so it needs no edit;
set `HUGO=` in the environment only to force a specific binary.

Check the paths at the top of `deploy.sh` match your box, then run it once:

```sh
/home/wosa/pivotce-src/deploy.sh
```

**Keeping it current**

Articles written through the CMS land in GitHub, not on your server, so
something has to bring them across. A cron entry is enough:

```cron
*/5 * * * * /home/wosa/pivotce-src/deploy.sh
```

`deploy.sh` exits immediately when the repo hasn't changed, so this costs
nothing on the vast majority of runs. A new article goes live within five
minutes of being published in the CMS.

**Building elsewhere instead**

If you would rather not install Hugo on the server, build on your laptop and
push the result up. The trailing slash on `public/` matters — it copies the
contents rather than creating `pivot/public/`:

```sh
hugo --minify --gc
rsync -az --delete public/ you@www.webosarchive.org:/home/wosa/wosa-web/pivot/
```

The tradeoff is that community posts then sit in GitHub until you next run it.

**GitHub Actions**

`.github/workflows/deploy.yml.disabled` does the same thing on GitHub's
runners. It is inert while it carries that extension. If you ever want it,
rename it to `deploy.yml` and add three repo secrets — `DEPLOY_KEY`,
`DEPLOY_KNOWN_HOSTS`, `DEPLOY_TARGET`. The cron approach above needs none of
that, so there is no reason to switch unless you want builds off your own box.

## 2. Server config

Each site on this host lives in its own directory under `/home/wosa/wosa-web/`,
and the `www.webosarchive.org` vhost roots at `.../wosa-web/webosarchive.org`.
The archive sits alongside it at `.../wosa-web/pivot`, outside that root, so the
`/pivot` URLs need pointing at it explicitly.

Use `root`, not `alias`. The URL prefix and the directory are both named
`pivot`, so `root /home/wosa/wosa-web` resolves `/pivot/x` to
`/home/wosa/wosa-web/pivot/x` by plain concatenation. `alias` would work for
static files but silently breaks PHP: `$document_root` then no longer matches
the served directory, so `$document_root$fastcgi_script_name` builds a path
that does not exist and nginx returns 404 for `menu.php` while every static
file keeps working.

Only URIs beginning with `/pivot` reach these blocks, so the sibling site
directories stay unreachable.

```nginx
# Bare /pivot -> /pivot/, otherwise it misses the prefix location below.
location = /pivot {
    return 301 $scheme://$host/pivot/;
}

location /pivot/ {
    root /home/wosa/wosa-web;
    # error_page, not `try_files ... /pivot/404.html`: naming the file in
    # try_files serves it with a 200, so every missing article would report
    # success to crawlers and to anything checking the archive for rot.
    error_page 404 /pivot/404.html;
    try_files $uri $uri/ =404;
}

# menu.php. This MUST appear before the vhost's generic `location ~ \.php$`:
# nginx tests regex locations in the order they are written and takes the
# first match, so a generic .php block defined earlier swallows these
# requests and resolves them against the vhost root -- 404 for menu.php
# while every static file under /pivot/ keeps working.
location ~ ^/pivot/.*\.php$ {
    root /home/wosa/wosa-web;
    include fastcgi_params;
    fastcgi_pass unix:/run/php/php-fpm.sock;   # copy from the existing PHP block
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
}

# Path-preserving redirect, so deep links survive.
location ^~ /pivotce/ {
    rewrite ^/pivotce/(.*)$ /pivot/$1 permanent;
}
location = /pivotce {
    return 301 $scheme://$host/pivot/;
}

# The CMS: https only (OAuth requires it), and not worth indexing.
location /pivot/admin/ {
    root /home/wosa/wosa-web;
    if ($scheme = http) { return 301 https://$host$request_uri; }
    try_files $uri $uri/ /pivot/admin/index.html;
}

# OAuth relay. The trailing slash strips the prefix, so Sveltia's
# <base_url>/auth reaches the relay's /auth. Without this block the request
# falls through to `location /pivot/` above and returns the site's own 404
# page, which looks like a broken login rather than a missing service.
location /pivot/oauth/ {
    if ($scheme = http) { return 301 https://$host$request_uri; }
    proxy_pass http://127.0.0.1:3000/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

Take `fastcgi_pass` verbatim from whichever block already serves `/menu.php` —
the socket path varies by PHP version.

```sh
grep -rn "fastcgi_pass" /etc/nginx/
sudo nginx -t && sudo systemctl reload nginx
curl -sI https://www.webosarchive.org/pivot/menu.php     # expect 200
```

Keep serving `/pivot/` over plain http as well as https. A large share of this
readership is on webOS 2.x/3.x, which cannot negotiate modern TLS; the archive
is public material with nothing to protect in transit. Only `/pivot/admin/` and
`/pivot/oauth/` force https.

### Redirects from the old hostnames

```nginx
server {
    listen 80;
    listen 443 ssl;
    server_name pivot.webosarchive.org pivotce.webosarchive.org;
    # $request_uri preserves the path, so a link to a specific article lands on
    # that article rather than the front page.
    return 301 $scheme://www.webosarchive.org/pivot$request_uri;
}
```

Keeping `$scheme` rather than forcing https matters here: an http-only device
following a redirect to https cannot complete it.

## 3. OAuth relay

Register a GitHub OAuth app under the **webOSArchive** org with callback
`https://www.webosarchive.org/pivot/oauth/callback`. Then install
[`vencax/netlify-cms-github-oauth-provider`](https://github.com/vencax/netlify-cms-github-oauth-provider)
(Decap-protocol compatible, which Sveltia speaks) alongside the site clone:

```sh
git clone https://github.com/vencax/netlify-cms-github-oauth-provider \
  /home/wosa/pivot-admin/cms-oauth
cd /home/wosa/pivot-admin/cms-oauth && npm ci --omit=dev
```

Put the credentials in `.env` in that directory, readable only by you:

```sh
cat > /home/wosa/pivot-admin/cms-oauth/.env <<'EOF'
OAUTH_CLIENT_ID=...
OAUTH_CLIENT_SECRET=...
EOF
chmod 600 /home/wosa/pivot-admin/cms-oauth/.env
```

That file sits inside a git clone, so keep it out of any commit:

```sh
echo '.env' >> /home/wosa/pivot-admin/cms-oauth/.git/info/exclude
```

```ini
# /etc/systemd/system/cms-oauth.service
[Unit]
Description=Sveltia CMS OAuth relay
After=network.target

[Service]
# Runs as wosa because the code lives under /home/wosa. A dedicated account
# would be better isolation but needs traverse rights all the way down, which
# is more moving parts than this earns.
User=wosa
WorkingDirectory=/home/wosa/pivot-admin/cms-oauth
Environment=NODE_ENV=production PORT=3000
Environment=ORIGINS=www.webosarchive.org
# systemd reads this as root before dropping privileges, so 600 is fine.
EnvironmentFile=/home/wosa/pivot-admin/cms-oauth/.env
ExecStart=/usr/bin/node index.js
Restart=on-failure

NoNewPrivileges=true
PrivateTmp=true
ProtectSystem=strict
# NOT ProtectHome=true: that hides /home entirely, and the service would fail
# to reach its own WorkingDirectory. read-only still denies writes, which is
# all this relay needs -- it holds no state.
ProtectHome=read-only

[Install]
WantedBy=multi-user.target
```

```sh
sudo systemctl daemon-reload
sudo systemctl enable --now cms-oauth
systemctl status cms-oauth
curl -sI localhost:3000/auth          # expect a redirect to github.com
```

Pin the version and read the source before trusting it — Sveltia's docs flag
third-party OAuth clients as unreviewed. The alternative is their Cloudflare
Worker: less to maintain, but an external dependency.

## 4. Contributor access

Access is GitHub org membership, so there is no user table on the server and no
password reset to compromise.

- **Write** on `webOSArchive/pivotce.com` → publishes directly.
- **Read** → `publish_mode: editorial_workflow` opens a pull request instead,
  so you review before anything goes live.

Contributors need a GitHub account; that is the one real cost of this design.

## 5. Local development

```sh
hugo server -D            # http://localhost:1313/pivot/
```

The nav bar will not appear locally: `wosa-menu.js` requests `/pivot/menu.php`,
which needs PHP. That is by design — a failed menu load leaves the site readable
rather than showing an empty bar.
