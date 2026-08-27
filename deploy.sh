#!/bin/sh
#
# Pull, build, publish. Safe to run from cron as often as you like: it does
# nothing at all unless the GitHub repo has actually changed.
#
#   /home/wosa/pivotce-src     git clone, outside the docroot
#   /home/wosa/wosa-web/pivot  what the web server serves -- build output only
#
set -eu

REPO=/home/wosa/pivotce-src
DOCROOT=/home/wosa/wosa-web/pivot
HUGO=/usr/bin/hugo

cd "$REPO"

git fetch --quiet --depth 1 origin main
if [ "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)" ]; then
    exit 0                      # nothing new; the normal case on most runs
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
