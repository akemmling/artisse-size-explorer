# Artisse size explorer - handover for any AI or new chat

Static web page (GitHub Pages: https://akemmling.github.io/artisse-size-explorer/) that turns the Artisse intrasaccular
device sizing sheet into a continuous width/height chart (scissor-braid model `H² + α²·W² = L²`, exact at the two published
points per device). Author: Prof. André Kemmling. DOI 10.5281/zenodo.22037111 (cite the archived version). Public repo:
nothing private, no patient data, no secrets in files.

- `index.html` - the explorer; self-contained (no build, no dependencies, works offline). Build stamp in `.version`.
- `background.html` - methods and sources. `og-card.png`, `sitemap.xml`, `CITATION.cff`, `LICENCE`.
- `googlea8408cbf96a1ebee.html`, `423954e651654dc4b69779f01a4993fb.txt` - site verification files; keep.
- `stats/community.json` - anonymous visitor counts, written every 6 hours by `.github/workflows/community-stats.yml`
  running `scripts/fetch_community_stats.py` (GoatCounter; token only as the Actions secret GOATCOUNTER_TOKEN).
- Deploy = push to main (Pages). Keep the disclaimer and the "not affiliated with Medtronic" notice on every page.
- Commit and push after each change; this repo is the only source.
