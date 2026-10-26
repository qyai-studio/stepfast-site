#!/usr/bin/env python3
"""Static site generator for stepfast marketing site. Stdlib only.
Usage: python3 build.py   ->  writes ./dist/"""
import html
import json
import shutil
from pathlib import Path

import config as C
from pages import PAGES

ROOT = Path(__file__).parent
DIST = ROOT / "dist"

NAV = [
    ("how-it-works", "/how-it-works/", "How it works"),
    ("intermittent-fasting", "/intermittent-fasting/", "Fasting"),
    ("walking-for-weight-loss", "/walking-for-weight-loss/", "Walking"),
    ("safety", "/safety/", "Safety"),
]


def esc(s):
    return html.escape(s, quote=True)


def url_for(slug):
    return f"{C.SITE_URL}/" + (slug + "/" if slug else "")


def jsonld(objs):
    return "".join(
        f'<script type="application/ld+json">{json.dumps(o, ensure_ascii=False)}</script>' for o in objs
    )


def org():
    return {"@type": "Organization", "@id": f"{C.SITE_URL}/#org", "name": C.PUBLISHER, "url": C.SITE_URL}


def structured_data(p):
    out = []
    if p["kind"] == "home":
        out.append({"@context": "https://schema.org", "@graph": [
            org(),
            {"@type": "WebSite", "@id": f"{C.SITE_URL}/#site", "name": C.SITE_NAME, "url": C.SITE_URL,
             "publisher": {"@id": f"{C.SITE_URL}/#org"}, "inLanguage": "en"},
            {"@type": "MobileApplication", "name": C.SITE_NAME, "operatingSystem": f"iOS {C.MIN_IOS}.0 or later",
             "applicationCategory": "HealthApplication", "downloadUrl": C.APP_STORE_URL,
             "publisher": {"@id": f"{C.SITE_URL}/#org"}, "description": p["description"]},
        ]})
    else:
        crumbs = [("Home", url_for(""))]
        parts = p["slug"].split("/")
        for i, part in enumerate(parts[:-1]):
            sub = "/".join(parts[: i + 1])
            match = next((q for q in PAGES if q["slug"] == sub), None)
            crumbs.append((match["h1"] if match else part.replace("-", " ").title(), url_for(sub) if match else None))
        crumbs.append((p["h1"], url_for(p["slug"])))
        crumbs = [c for c in crumbs if c[1]]
        out.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
        if p["kind"] == "article":
            out.append({"@context": "https://schema.org", "@type": "Article", "headline": p["h1"],
                        "description": p["description"], "mainEntityOfPage": url_for(p["slug"]),
                        "dateModified": C.UPDATED, "datePublished": C.UPDATED,
                        "author": {"@type": "Organization", "name": f"{C.SITE_NAME} team"},
                        "publisher": {"@type": "Organization", "name": C.PUBLISHER}})
    return jsonld(out)


def breadcrumbs(p):
    if p["kind"] == "home":
        return ""
    parts = ['<a href="/">Home</a>']
    segs = p["slug"].split("/")
    for i in range(len(segs) - 1):
        sub = "/".join(segs[: i + 1])
        match = next((q for q in PAGES if q["slug"] == sub), None)
        if match:
            parts.append(f'<a href="/{sub}/">{esc(match["h1"])}</a>')
    parts.append(esc(p["h1"]))
    return f'<nav class="crumbs" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'


def header(p):
    nav_items = []
    for key, href, label in NAV:
        current = ' aria-current="page"' if p.get("nav") == key else ""
        nav_items.append(f'<a href="{href}"{current}>{label}</a>')
    links = "".join(nav_items)
    return (f'<a class="skip" href="#main">Skip to content</a><header class="site-header"><div class="wrap">'
            f'<a class="brand" href="/">{C.SITE_NAME}</a><nav class="nav" aria-label="Main">{links}'
            f'<a href="{C.app_link("nav")}" rel="noopener">App Store</a></nav></div></header>')


def footer():
    contact = f' · <a href="mailto:{esc(C.CONTACT_EMAIL)}">{esc(C.CONTACT_EMAIL)}</a>' if C.CONTACT_EMAIL else ""
    return (f'<footer class="site-footer"><div class="wrap"><nav aria-label="Footer">'
            f'<a href="/how-it-works/">How it works</a><a href="/intermittent-fasting/">Intermittent fasting</a>'
            f'<a href="/walking-for-weight-loss/">Walking</a><a href="/tools/step-goal/">Step goal planner</a>'
            f'<a href="/safety/">Safety</a><a href="{C.LEGAL_PRIVACY}">Privacy</a><a href="{C.LEGAL_TERMS}">Terms</a></nav>'
            f'<p>StepFast is published by {C.PUBLISHER}{contact}. For adults {C.MIN_AGE} and older. '
            f'StepFast is a wellness app, not a medical device. It does not give medical advice, diagnose or treat any condition. '
            f'Talk to a doctor before changing how you eat or exercise.</p>'
            f'<p>App Store is a service mark of Apple Inc.</p></div></footer>')


def render(p):
    body = p["body"]()
    canonical = url_for(p["slug"])
    if p["kind"] == "home":
        main = f'<main id="main" class="wrap">{body}</main>'
    else:
        review = (f'<p class="meta">{esc(C.REVIEWER)} · Updated {C.UPDATED}</p>' if C.REVIEWER else
                  f'<p class="meta">Written by the {C.SITE_NAME} team · Updated {C.UPDATED} · Not medical advice</p>')
        main = (f'<main id="main" class="wrap narrow">{breadcrumbs(p)}<h1>{esc(p["h1"])}</h1>{review}{body}</main>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["description"])}">
<link rel="canonical" href="{canonical}">
<meta name="apple-itunes-app" content="app-id={C.APP_ID}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{C.SITE_NAME}">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["description"])}">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#f9d84b">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Ccircle cx='16' cy='16' r='15' fill='%23f9d84b'/%3E%3Cpath d='M9 20l4-8 4 6 3-5 3 7' fill='none' stroke='%2314110a' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="stylesheet" href="/static/style.css">
{structured_data(p)}
</head>
<body>
{header(p)}
{main}
{footer()}
<script src="/static/app.js" defer></script>
</body>
</html>
"""


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST / "static")
    if (ROOT / "CNAME").exists():
        shutil.copy2(ROOT / "CNAME", DIST / "CNAME")
    for p in PAGES:
        out = DIST / p["slug"] / "index.html" if p["slug"] else DIST / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p), encoding="utf-8")
    urls = "".join(
        f"<url><loc>{url_for(p['slug'])}</loc><lastmod>{C.UPDATED}</lastmod></url>" for p in PAGES
    )
    (DIST / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n',
        encoding="utf-8")
    (DIST / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {C.SITE_URL}/sitemap.xml\n", encoding="utf-8")
    nf = {"slug": "404", "title": "Page not found | StepFast", "description": "This page does not exist.",
          "h1": "Page not found", "kind": "page", "nav": None,
          "body": lambda: '<p>That page does not exist. <a href="/">Go to the home page</a>.</p>'}
    page = render(nf).replace('<link rel="canonical" href="' + url_for("404") + '">', '<meta name="robots" content="noindex">')
    (DIST / "404.html").write_text(page, encoding="utf-8")
    print(f"Built {len(PAGES)} pages into {DIST}")


if __name__ == "__main__":
    main()

