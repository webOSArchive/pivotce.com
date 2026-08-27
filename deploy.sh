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

REPO=/home/wosa/pivotce-src
DOCROOT=/home/wosa/wosa-web/pivot
HUGO=/usr/bin/hugo

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
git reset --hard --quiet origin/main

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
