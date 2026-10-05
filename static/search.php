<?php
/*
 * Sidebar search: hands the query to DuckDuckGo Lite, limited to this site.
 *
 * The form submits here rather than straight to DuckDuckGo so the site:
 * restriction is added server-side -- a hidden field can't prepend to the
 * user's own text, and doing it in script would leave readers without
 * JavaScript searching the whole web. This only redirects; it never fetches
 * from DuckDuckGo, which treats a server relaying queries as a bot.
 *
 * DDG Lite is plain HTML with no script, so it suits webOS browsers. It is
 * https-only (TLS 1.2+), which those browsers now handle.
 */
$q = isset($_GET['q']) ? trim((string)$_GET['q']) : '';

if ($q === '') {
    header('Location: ./', true, 302);
    exit;
}

// Generous for a search box, but stops the redirect URL growing unbounded.
if (function_exists('mb_substr')) {
    $q = mb_substr($q, 0, 200, 'UTF-8');
} else {
    $q = substr($q, 0, 200);
}

$url = 'https://lite.duckduckgo.com/lite/?q='
     . rawurlencode('site:www.webosarchive.org/pivot ' . $q);
header('Location: ' . $url, true, 302);
