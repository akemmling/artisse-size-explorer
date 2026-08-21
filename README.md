# Dynamic size explorer for the Artisse™ Intrasaccular Device

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.22037111.svg)](https://doi.org/10.5281/zenodo.22037111)

**→ [Open the explorer](https://akemmling.github.io/artisse-size-explorer/)**  ·  [Background & methods](https://akemmling.github.io/artisse-size-explorer/background.html)  ·  [Video walkthrough](https://youtu.be/-nHWv_m5mf4)

An interactive sizing chart for the Artisse™ intrasaccular device (Medtronic). The printed
sizing sheet can only list a handful of fixed compression/height pairs per device. This page
turns that into a continuous one: move a slider to any aneurysm width and read the device's
compressed height, for all twenty Artisse sizes.

Enter a measured aneurysm width and dome-to-neck height and the tool flags up to three devices
whose compressed shape is likely to fit, showing the resulting width compression and the
protrusion into the neck.

## How it works, in one paragraph

A braided nitinol mesh conserves filament length: squeeze it narrower and it gets taller.
Treating the braid as a scissor mesh gives `H² + α²·W² = L²`. The Medtronic sizing sheet
publishes exactly two shapes per device — nominal width and height in air, and the compressed
height at the rated maximum average aneurysm width — which is two points for the two unknowns
`α` and `L`, so the curve through them is exact at both. Everything between and beyond those
two widths is a model estimate. The [background page](https://akemmling.github.io/artisse-size-explorer/background.html)
sets this out step by step and names where every number comes from.

## Important

Only the two published endpoints per device are manufacturer figures. Every value between and
beyond them is an unvalidated estimate from a simplified model and has not been clinically
verified. This tool is for education and research; it does not replace the current Instructions
for Use, your own measurements, or professional consultation. The full disclaimer is at the
bottom of each page.

Not affiliated with, sponsored by, or endorsed by Medtronic. Artisse is a trademark of Medtronic.

## Files

| File | Purpose |
|---|---|
| `index.html` | The explorer. Self-contained: no build step, no dependencies, no network requests — open the file and it works offline. |
| `background.html` | Model, data provenance, per-device fitted parameters, caveats. |
| `og-card.png` | Social/link preview image. |
| `sitemap.xml` | For search-engine submission. |

## Citation

Kemmling A. *Dynamic size explorer for the Artisse™ Intrasaccular Device.* Zenodo.
[doi:10.5281/zenodo.22037111](https://doi.org/10.5281/zenodo.22037111)

The DOI above is the concept DOI: it always resolves to the newest version. Each release also
gets its own version DOI if you need to point at an exact snapshot.

## Author

Prof. Dr. André Kemmling, Clinic for Neuroradiology, University Hospital Marburg (UKGM), Germany
· <kemmling@uni-marburg.de>

## Licence

See [`LICENCE`](LICENCE). © 2026 André Kemmling.
