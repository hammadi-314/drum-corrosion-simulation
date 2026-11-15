# H₂S Reference-Field / Numerical 3D Viewer — Revolver Pig Magazine

This package upgrades the earlier GitHub-ready `.glb` drum viewer with face-by-face numerical readouts. Select each proposed material label (Al 6061-T6, Al 7075-T6, AISI 1020 normalized, AISI 304, AISI 316), choose a view field, and click the 3D surface for a local reading.

## How to open

This is a static site suitable for GitHub Pages. Extract the ZIP and upload all of `index.html`, `models/`, and `data/` to a repository. In repository **Settings → Pages**, select **Deploy from a branch**, `main`, root. The site loads THREE.js from a CDN, so internet access is required. Local `file://` often blocks the `fetch` call for the numerical data. To view locally, run `python -m http.server 8000` inside this directory and visit `http://localhost:8000`.

## How the numerical values were obtained

**These are numeric values calculated from a mapped 316L literature reference field, not an electrochemical corrosion simulation of the five alloys.**  The uploaded STEP was tessellated into 12,080 triangles, retaining the 10 individual solids. Each face of the triangulated CAD model was matched to the GLB mesh by its center (maximum matching distance less than 0.001 mm). The existing surface-field data (`drum_AISI_316_REFERENCE_NOT_PREDICTION.vtp`) supplies an assumed corrosion rate for each triangle.

- Assumed dry external faces: `0 mm/year` *only because we assume they do not contact sour liquid*; this is not intrinsic material resistance.
- Assumed wet chamber faces: reference rate from `0.70` to `~2.39935 mm/year`, according to a hypothetical lower-interior-chamber hotspot interpolation (maximum published PIT rate 2.4 mm/year). This spatial interpolation is **not** a model of fluid mechanics or electrochemistry.
- Penetration (mm): rate(mm/year) × exposure days / 365.
- Remaining chamber wall (mm): nominal 10.0 mm − penetration (mm). This assumes simple one-sided metal loss and ignores geometric redistribution, stress, cracks, and corrosion products.
- The min/max refer to **wetted triangle samples on the selected chamber(s)**, not the global min including dry faces (which is 0).
- Default: 7 days. 30, 90, and 365-day options are **illustrative linear what-if cases**, not time-evolving predictions.
- All five material selections use **the same** field and therefore must not be interpreted as an alloy ranking.

## What the viewer provides

1. 3D GLB models for all five candidate material labels.
2. Minimum and maximum local corrosion reference rate (mm/year), penetration (mm), or nominal remaining wall thickness (mm).
3. Minimum remaining chamber wall, maximum penetration, and six-chamber comparison table.
4. Click-to-inspect local reference rate, penetration, wall thickness, surface location, exposure assumption, and triangle ID.
5. Numeric color bar and CSV export of the displayed assumptions.
6. Numerical triangle-by-triangle CSV (`data/triangle_reference_field.csv`) and exact source field arrays (`data/face_fields.json`).

## Benchmark research

Shah et al., **Corrosion Behavior of AISI 316L Stainless Steel in a Highly Sour Environment**, Trends in Sciences, 2022, https://doi.org/10.48048/tis.2022.4642 . Their sour test was at 60°C, 3 bar partial H₂S, 30 bar total, 5 wt% NaCl + 0.5 wt% acetic acid, ~7 days. 316L uniform corrosion rate = 0.70 ± 0.03 mm/year; deepest pit = 46.81 µm in 7 days; pit penetration rate ~2.4 mm/year. **316L is not identical to AISI 316**.

Independent conditions reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7399776/ .

## What this is NOT

No genuine galvanic/electrochemical FEA, CFD, finite-element stress/displacement, H₂S sulfide-stress cracking, hydrogen-induced cracking, verified corrosion behavior for Al 6061-T6 / Al 7075-T6 / AISI 1020 normalized / AISI 304 / AISI 316, physical metal removal from original CAD, service-life prediction, or ISO 15156 sour qualification. The tool is explicitly a *reference-field sensitivity visualization* for identifying potentially vulnerable chamber surfaces and for planning follow-up tests.

Do not call these numbers five **material-specific simulation results** in a scientific report. Real comparative material results require matched sour-water test rates/kinetics or a validated material-specific corrosion model.
