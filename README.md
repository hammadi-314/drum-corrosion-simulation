# Five-Material Sour Corrosion Sensitivity Study — Revolver Drum v4.0

**Live 3D viewer:** https://hammadi-314.github.io/drum-corrosion-simulation/

## What this model is

A transparent **numerical surface recession sensitivity study** using the user-supplied 10-solid revolver drum model. Full exposure is assigned to all **12,080 GLB/STEP surface triangles**, totaling **27.293367 m²**, across six chambers, two end plates and two hubs. All inside and outside faces are included.

Different selectable material and rate scenarios now produce **different numerical results**, unlike the previous viewer where all five grades inherited the same 316L benchmark. The analysis numerically integrates assigned metal loss one day at a time; the 3D mesh itself is **not physically eroded**. Color intensity is scaled against the **same five-material maximum** at each scenario for an interpretable comparison.

## Why these are engineering scenarios, not five validated rates

The published 316L corrosion reference is 0.74 mm/year in 60 °C, 3 bar H₂S, 30 bar total, 5 wt% NaCl + 0.5 wt% acetic acid, approximately seven days. **316L differs from AISI 316**. The other material scenarios are not measured in this identical environment. Published sour/acid-chloride data supports qualitative differences, but no matched five-alloy study was established.

Every low/central/high rate shown below is an **explicit chosen numerical sensitivity input**, **not a published rate in the specified sour solution**, except the central **316L-derived** benchmark.

| Material | Low (mm/y) | Central (mm/y) | High (mm/y) | Interpretation |
| --- | ---: | ---: | ---: | --- |
| Al 6061-T6 | 0.09 | 0.50 | 2.00 | Sensitivity assumptions; source measured 0.0881 mm/y in **gaseous** H₂S at 75 °C, NOT the chosen wet condition |
| Al 7075-T6 | 0.15 | 0.90 | 3.00 | Sensitivity assumptions; chloride studies show greater susceptibility than 6061 under some conditions |
| AISI 1020 normalized | 0.70 | 3.00 | 8.00 | Sensitivity assumptions; sour-steel rates vary strongly with pH, temperature, flow and corrosion-product scale |
| AISI 304 | 0.50 | 1.20 | 3.00 | Sensitivity assumptions; controlled H₂S study found generally lower attack on 316L than 304L, not these exact rates |
| AISI 316 | 0.37 | 0.74 | 1.48 | Center extrapolated from **316L** experiment; low/high are hypothetical half/double multipliers |

These intervals do **not** represent confidence intervals or statistically estimated probabilities.

## Equations and implementation

At each triangular CAD face, define a local severity fraction from the preceding illustrative CAD hotspot template `face_fields.json`, on the interval 0 to 1. No hotspot location has been solved or empirically determined for the actual drum.

For each material `m`, rate-case `c`, and face `i`:

```text
hotspot_i  = clamp((previous_reference_rate_i - 0.700) / (2.399351 - 0.700), 0, 1)
common_pit_ratio = 2.4 / 0.74 = 3.243243
local_rate_i = assumed_uniform_rate_[m,c] * (1 + (common_pit_ratio - 1) * hotspot_i)
loss_i(t+1 day) = loss_i(t) + local_rate_i / 365
remaining_nominal_chamber_wall_i = 10.0 - loss_i
```

The common pitting multiplier uses two separate reported 316L measurements and is a **what-if multiplier**, NOT a universal material-specific pit rate. The 10 mm thickness is the uploaded chamber CAD wall; the end plates and hubs do not inherit this wall thickness. The computation uses constant rates over selected durations, **not electrochemical PDE/FEM, process-fluid CFD, metal geometry erosion or structural FEA**.

> Any 30, 90 or 365 day result is a constant-rate sensitivity extrapolation far beyond the 7 day reference, not a tested life forecast.

## Seven-day results — CENTRAL sensitivity case

| Material | Min uniform loss (mm) | Max localized-sensitivity loss (mm) | Min remaining chamber wall (mm) |
| --- | ---: | ---: | ---: |
| Al 6061-T6 | 0.0096 | 0.0311 | 9.9689 |
| Al 7075-T6 | 0.0173 | 0.0560 | 9.9440 |
| AISI 1020 normalized | 0.0575 | 0.1866 | 9.8134 |
| AISI 304 | 0.0230 | 0.0746 | 9.9254 |
| AISI 316 | 0.0142 | 0.0460 | 9.9540 |

**Do not interpret this order as a measured five-alloy corrosion ranking.** In particular, the favorable-looking 6061 scenario is not an evidence-based demonstration of 6061 performance in wet H₂S.

## How to use the GitHub viewer

Choose material, rate case (low, central, high), visualized value (local rate, recession, wall), exposure duration (7, 30, 90, 365 days), and part. Rotate/zoom the 3D model, click any visible face for its numerical scenario values, and inspect the full ten-body table. Click a material row in the comparison table to switch its 3D model. The front plate starts hidden to show chambers but is still included in exposure metrics.

`Export readings CSV` downloads calculated results for **all five materials and all ten components** at the current case and duration.

### Reproducing the numerical run

- `material_scenarios_v4.json`: the five input rate triplets, source notes, and assumptions
- `face_fields.json`: the 12,080-face geometry-aligned hotspot template, now fully exposed
- `simulate_corrosion_v4.py`: independent open-source Python reproduction of the face-by-face one-day time integration
- `simulation_results_v4.csv`: 60 summary scenario rows (5 materials × 3 cases × 4 durations)
- `triangle_reference_field.csv`: original all-surface base template, **not material-specific**; see the actual viewer or simulation script for new material-dependent rates
- `drum_*.glb`: 3D assets from user-supplied STEP; surface is colored but not physically corroded

## Conclusions for senior design

1. **Design sensitivity**: depending on assumed rates, identical 10 mm chamber wall geometry gives substantially different seven-day recession. Carbon-steel and stainless/aluminum scenarios overlap in uncertainty; the exercise is a sensitivity assessment, not a final materials winner.
2. **Architecture improvements**: protect all wettable inner/outer chamber faces, end plates, shaft/hub interfaces and fasteners; use compatible sour-service coatings/sealing, remove persistent aqueous pockets where practicable, and ensure access for inspection and drainage.
3. **Selection decision**: retain qualified corrosion-resistant materials as candidates, but do NOT select 6061 or 316 solely because a model field is small. At the chosen **3 bar H₂S** with acidic chloride, the actual standard applicability envelope and cracking susceptibility require engineering review. **316/316L are not automatically ISO 15156-compliant** at these conditions.
4. **Next validation gate**: obtain the true field temperature, H₂S partial pressure, chloride, pH and liquid/wetting assumptions. Commission matched-condition sour-corrosion coupon/pitting tests for candidate grades (including their exact heat treatment, coating/weld state) and separate SSC/HIC qualification as necessary. Recalibrate the numerical rates and then rerun structural FEA with credible damage geometries.

## Source bibliography

- Shah et al. (2020), 316L test with/without 3 bar H₂S: https://pmc.ncbi.nlm.nih.gov/articles/PMC7399776/
- Shah et al. (2022), 316L pitting in highly sour service: https://doi.org/10.48048/tis.2022.4642
- Davoodi et al. (2011), 304L vs 316L in H₂S acidic media: https://doi.org/10.1016/j.corsci.2010.09.050
- Yang et al. (2022), 6061 H₂S gas/liquid behavior: https://doi.org/10.1080/00986445.2022.2030729
- Zhang et al., AISI-1020 CO₂/H₂S corrosion at 60 °C: https://www.sciencedirect.com/science/article/pii/S0042207X21007363
- 6061-T6 vs 7075-T6 chloride exposure research: https://www.sciencedirect.com/science/article/pii/S0013468616306946
- TWI, 316/316L sour-service limits and weld considerations: https://www.twi-global.com/technical-knowledge/published-papers/sour-service-limits-of-dual-certified-316-316l-austenitic-stainless-steel-and-weldments-march-2010

**Engineering safety disclaimer:** This is **not** a pressure-boundary qualification, safe-life calculation, H₂S cracking prediction, or certification to any oil-and-gas material standard.
