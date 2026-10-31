# Artisse size explorer - handover for any AI or new chat

Static web page (GitHub Pages: https://artisse-size-explorer.ak-apps.de/) that turns the Artisse intrasaccular
device sizing sheet into a continuous width/height chart (scissor-braid model `H² + α²·W² = L²`, exact at the two published
points per device). Author: Prof. André Kemmling. DOI 10.5281/zenodo.22037111 (cite the archived version). Public repo:
nothing private, no patient data, no secrets in files.

- `index.html` - the explorer; self-contained (no build, no dependencies, works offline). Build stamp in `.version`.
- `background.html` - methods and sources. `og-card.png`, `sitemap.xml`, `CITATION.cff`, `LICENCE`.
- `googlea8408cbf96a1ebee.html`, `423954e651654dc4b69779f01a4993fb.txt` - site verification files; keep.
- `stats/community.json` - anonymous visitor counts, written every 6 hours by `.github/workflows/community-stats.yml`
  running `scripts/fetch_community_stats.py` (GoatCounter; token only as the Actions secret GOATCOUNTER_TOKEN).
- Deploy = push to main (Pages). Custom domain `artisse-size-explorer.ak-apps.de` since 2026-10-20: `CNAME` file in the repo + a DNS-only CNAME to akemmling.github.io in the ak-apps.de zone (Cloudflare, account akemmling@gmail.com). The old akemmling.github.io/artisse-size-explorer/ address redirects. Keep the disclaimer and the "not affiliated with Medtronic" notice on every page.
- Commit and push after each change; this repo is the only source.
- Growth plan (2026-10-31, ~/Downloads/artisse-growth-plan_v1.md, review due 2026-11-28): the device table is JS-rendered, so the static "published numbers" section (20-size table, FAQ, FAQPage JSON-LD) and `llms.txt` exist for crawlers and AI assistants; keep them in sync with the `devices` array. Videos the user sends get a VideoObject entry each.
