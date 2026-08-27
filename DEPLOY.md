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

```sh
# Hugo is a single binary with no runtime dependencies.
sudo apt install hugo          # or grab the extended release from GitHub
hugo version                   # needs 0.146+ for the layouts/_markup hooks

sudo git clone --depth 1 https://github.com/webOSArchive/pivotce.com /home/wosa/pivotce-src
sudo mkdir -p /home/wosa/wosa-web/pivot
```

Check the paths at the top of `deploy.sh` match your box, then run it once:

```sh
sudo /home/wosa/pivotce-src/deploy.sh
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

Almost nothing to add. The existing rules already serve static files and PHP;
`/pivot/` inherits both. Two additions:

```nginx
# The CMS: https only (OAuth requires it) and not worth indexing.
location /pivot/admin/ {
    if ($scheme = http) { return 301 https://$host$request_uri; }
    try_files $uri $uri/ /pivot/admin/index.html;
}

# OAuth relay. The trailing slash strips the prefix, so Sveltia's
# <base_url>/auth reaches the relay's /auth.
location /pivot/oauth/ {
    if ($scheme = http) { return 301 https://$host$request_uri; }
    proxy_pass http://127.0.0.1:3000/;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-Proto $scheme;
}
```

And a 404 for the subtree, so a bad `/pivot/...` URL gets the archive's own
page rather than the main site's:

```nginx
location /pivot/ {
    try_files $uri $uri/ /pivot/404.html;
}
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
`https://www.webosarchive.org/pivot/oauth/callback`. Then deploy
[`vencax/netlify-cms-github-oauth-provider`](https://github.com/vencax/netlify-cms-github-oauth-provider)
(Decap-protocol compatible, which Sveltia speaks) to `/opt/cms-oauth`:

```ini
# /etc/systemd/system/cms-oauth.service
[Unit]
Description=Sveltia CMS OAuth relay
After=network.target

[Service]
User=cmsoauth
WorkingDirectory=/opt/cms-oauth
Environment=NODE_ENV=production PORT=3000
Environment=ORIGINS=www.webosarchive.org
EnvironmentFile=/etc/cms-oauth.env      # OAUTH_CLIENT_ID, OAUTH_CLIENT_SECRET; chmod 600
ExecStart=/usr/bin/node index.js
Restart=on-failure
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
PrivateTmp=true

[Install]
WantedBy=multi-user.target
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
