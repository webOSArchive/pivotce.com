#!/bin/sh
#
# Pull, build, publish. Safe to run from cron as often as you like: it does
# nothing at all unless there is something new to publish.
#
#   /home/wosa/pivotce-src     git clone, outside the docroot
#   /home/wosa/wosa-web/pivot  what the web server serves -- build output only
#
# Pass --force to rebuild and republish regardless.
#
set -eu

# Absolute path to this script, resolved before any cd so the re-exec below
# works however we were invoked.
SELF=$(cd "$(dirname "$0")" && pwd)/$(basename "$0")

REPO=/home/wosa/pivotce-src
DOCROOT=/home/wosa/wosa-web/pivot

# Find Hugo. The official .deb installs to /usr/local/bin while distro packages
# use /usr/bin, and cron does not share your shell's PATH -- so look in both
# rather than hardcode one. Override by setting HUGO= in the environment.
if [ -z "${HUGO:-}" ]; then
    for candidate in /usr/local/bin/hugo /usr/bin/hugo; do
        if [ -x "$candidate" ]; then HUGO=$candidate; break; fi
    done
fi
[ -n "${HUGO:-}" ] || HUGO=$(command -v hugo 2>/dev/null || true)
if [ -z "${HUGO:-}" ] || [ ! -x "$HUGO" ]; then
    echo "pivotce deploy: hugo not found in /usr/local/bin, /usr/bin or PATH" >&2
    exit 1
fi

cd "$REPO"
mkdir -p "$DOCROOT"

# The render hooks in layouts/_markup/ -- which prefix every in-article link and
# image with the /pivot subpath -- need Hugo 0.146+. An older Hugo builds with no
# error and silently emits links that escape the subdirectory, which the page
# count below cannot detect. Fail loudly instead.
ver=$("$HUGO" version | sed -n 's/.*hugo v\([0-9][0-9]*\)\.\([0-9][0-9]*\).*/\1 \2/p')
if [ -n "$ver" ]; then
    # shellcheck disable=SC2086
    set -- $ver
    if [ "$1" -eq 0 ] && [ "$2" -lt 146 ]; then
        echo "pivotce deploy: Hugo 0.$2 is too old, need 0.146+ (apt ships 0.92)" >&2
        exit 1
    fi
fi

git fetch --quiet --depth 1 origin main

# Rebuild when the repo has moved, when the docroot has never been populated
# (the first run after a fresh clone, where HEAD already matches origin), or
# when asked. Checking only git would leave a fresh clone doing nothing.
if [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ] \
   && [ -f "$DOCROOT/index.html" ] \
   && [ "${1:-}" != "--force" ]; then
    exit 0                      # nothing to do; the normal case on most runs
fi

# The server never has local edits, so a hard reset is the honest way to match
# the repo -- it can't leave a half-merged working tree behind.
#
# But the reset rewrites THIS script, and /bin/sh reads a script incrementally
# by byte offset: continuing after the file changes underneath us executes
# whatever now sits at that offset, with the old variables still set. Re-exec
# if we changed. This terminates -- on the second pass HEAD already matches
# origin, so the reset is a no-op and the checksums agree.
before=$(cksum < "$SELF")
git reset --hard --quiet origin/main
if [ "$before" != "$(cksum < "$SELF")" ]; then
    # --force, not "$@": the reset above has already moved HEAD to origin/main,
    # so a plain restart would see "nothing new" plus a populated docroot and
    # exit without building -- silently skipping the deploy of the very commit
    # that updated this script.
    echo "pivotce deploy: deploy.sh was updated, restarting with the new version"
    exec "$SELF" --force
fi

"$HUGO" --minify --gc --cleanDestinationDir --quiet

# Never publish a truncated build over the live archive. The archive alone is
# ~590 pages; far below that means the build silently lost content.
count=$(find public -name index.html | wc -l)
if [ "$count" -lt 500 ]; then
    echo "pivotce deploy: only $count pages built, refusing to publish" >&2
    exit 1
fi

rsync -a --delete public/ "$DOCROOT/"
echo "pivotce deploy: published $count pages to $DOCROOT"
