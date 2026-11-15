# H₂S Sour-Service Reference Mapping — Six-Chamber Revolver Drum

**Version 3.0: all surfaces exposed**, internal and external, across the uploaded 10-solid STEP assembly. Interactive 3D viewer and numerical reference fields for six chambers, both end plates, and two hubs.

**Live viewer:** https://hammadi-314.github.io/drum-corrosion-simulation/

## What changed

The earlier assumption that external faces and drum supports were dry has been removed. **Every one of the 12,080 triangular CAD faces is treated as contacting sour service**, including the outside and inside of all six chambers and every modeled exterior surface of the end plates and hubs. This is an exposure **assumption provided by the project**, not a fluid-dynamics prediction.

- Exposed mesh area (triangulated): **27.293367 m²**.
- Assigned everywhere: **0.70 mm/year** uniform corrosion-rate reference from a **316L** seven-day sour-service study.
- On selected lower-interior chamber triangles: a previously supplied **illustrative spatial hotspot** ranges up to **2.399351 mm/year**, capped by a separately reported **2.4 mm/year maximum pit-penetration rate**. **Neither its location nor geometry is independently predicted.** All other exterior and interior faces use the 0.70 mm/year baseline.
- Min/max of the numerical field: **0.70–2.399351 mm/year**, reflecting the **assumed field**, not solved electrochemistry.
- Penetration in mm = rate (mm/year) × duration (days)/365.
- Six chamber tubes: nominal 10 mm initial wall; example remaining wall estimate = 10 − assigned penetration. This is a single-surface arithmetic illustration **not** a pressure-rating, structural-strength, cracking or remaining-life assessment.
- For end plates and hubs, remaining wall is deliberately marked **N/A**, since their thickness is not assumed to be 10 mm.
- Default 7 days matches the research duration. Longer durations are **unvalidated linear what-if calculations**, not service-life predictions.

## Open and use

GitHub Pages serves `index.html` from the root. `face_fields.json` and the five `drum_...glb` models are stored in the **root of this repository**. The website also supports an alternate `data/` and `models/` layout as fallback.

Choose a material label, output field, exposure duration, and inspected part. You can orbit and zoom the 3D assembly; click surfaces to see an individual triangle's assigned rate, penetration and coordinates. The front end plate is initially hidden in the visualization to make the chamber interiors visible; it **remains included in the exposure dataset**, and you can toggle it back on.

The **10-body table** reports minimum and maximum assigned penetration and the exposed surface area. **Export readings CSV** exports all 10 parts. Other datasets:

- `face_fields.json`: reference rates and assumed exposure classes for each of 12,080 triangles.
- `triangle_reference_field.csv`: matching face-by-face values and triangle areas, now updated to all-surface exposure.
- `chamber_summary_7d.csv`: 7-day reference summary, including the plates and hubs.
- `drum_*.glb`: original triangulated geometry used by the webpage; **no physical corrosion erosion has been generated**.

## What the five material selections do *not* mean

Material dropdown labels: **Al 6061-T6, Al 7075-T6, AISI 1020 normalized, AISI 304 and AISI 316.** Each displays the same 316L-sourced corrosion-reference field; the model **cannot** compare corrosion resistance of these materials. The reference material **316L is not identical to AISI 316**. No material-specific electrochemical H₂S analysis has been run.

## Research basis and limitations

Shah et al., *Corrosion Behavior of AISI 316L Stainless Steel in a Highly Sour Environment*, Trends in Sciences, 2022: https://doi.org/10.48048/tis.2022.4642

Literature test conditions cited by the viewer: **60 °C, 3 bar H₂S partial pressure, 30 bar total pressure, 5 wt% NaCl, 0.5 wt% acetic acid, approximately 7 days**; 316L corrosion rate approximately **0.70 ± 0.03 mm/year**, measured deepest pit **0.04681 mm** after seven days, approximately **2.4 mm/year** pit rate.

**Not performed:** electrochemical FEM, fluid/wetting CFD, pitting initiation prediction, material-specific sour corrosion kinetics, H₂S sulfide-stress cracking or hydrogen-induced cracking evaluation, structural FEA, real material removal, ISO 15156 sour-service qualification, or lifetime prediction.

The purpose is an **illustrative full-coverage corrosion-reference visualization** for identifying exposed areas and planning additional engineering tests, not proof of sour-service suitability or a ranking of materials.
