# Revolver drum · Published-material corrosion benchmark viewer (v6.0)

**Live interactive 3D viewer:** https://hammadi-314.github.io/drum-corrosion-simulation/?v=6.0

## Critical interpretation

The five corrosion-rate inputs now come from **published experimental results or a clearly documented conversion of a published corrosion current**, rather than arbitrary low/central/high values. The **Low / Central / High dropdown has been removed**. Source conditions vary significantly. **These five values are NOT from a matched five-alloy 60°C, 3 bar H₂S experiment.** No rank of actual sour-service suitability, ISO 15156 conformity, stress-corrosion-cracking susceptibility, pressure integrity or service life can be inferred.

The CAD is the user-supplied ten-body revolver magazine with six chambers, two end plates and two hubs (12,080 surface triangles; 27.293367 m² including interior and exterior). The mesh is colored to show modeled corrosion, but metal is **not geometrically eroded**.

## Five source-traceable material inputs

| Candidate dropdown | Paper's actual specimen / method | Input rate (mm/year) | Tested environment |
| --- | --- | ---: | --- |
| Al 6061-T6 | Uncoated 6061-T6; polarization current **9.47 µA/cm²** converted using ASTM G102-type Faraday calculation | **0.1031524** (calculated, not paper-reported penetration) | 3.5 wt% NaCl, **no H₂S** |
| Al 7075-T6 | Uncoated 7075-T6; polarization current **0.31 µA/cm²** converted in the same way | **0.0032445** (calculated, not paper-reported penetration) | Same 3.5 wt% NaCl study as 6061-T6, **no H₂S** |
| AISI 1020 normalized candidate | AISI 1020, heat-treatment state not confirmed; 2400-grit polished specimen, weight loss | **0.58** (measured; 0.92 mm/y was reported for the rougher 100-grit finish) | 25°C, CO₂-saturated 3 wt% NaCl, pH ~5, static immersion, 168 h; **no H₂S** |
| AISI 304 | Uncoated 304 stainless substrate, figure from published abstract | **0.17** (author-reported; full paper test details not independently verified) | H₂S-containing simulated oil-and-gas environment, precise temperature and H₂S pressure not verified |
| AISI 316 candidate | **316L** specimen (not exact 316), measured weight-loss | **0.74** (measured for 316L only) | 60°C, 3 bar H₂S partial pressure, 30 bar total, 5 wt% NaCl, 0.5 wt% acetic acid, approximately 7 d |

**Source URLs:**

1. Al 6061-T6 and Al 7075-T6: [Materials 2024, 17, 4285 — Table 3 uncoated (asterisk) specimens](https://www.mdpi.com/1996-1944/17/17/4285), DOI 10.3390/ma17174285.
2. [ASTM G102-23](https://store.astm.org/standards/g102) — corrosion-current to uniform penetration-rate methodology.
3. [Mohammed et al., 2026, Table 5](https://www.iieta.org/journals/ijdne/paper/10.18280/ijdne.210410) — 1020 CO₂-brine corrosion rates and surface finish.
4. [Huang et al., 2023](https://doi.org/10.1007/s12666-023-02986-2) — 304 stainless substrate H₂S-environment benchmark from abstract.
5. [Shah et al., 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7399776/) — 316L weight-loss at 3 bar H₂S.
6. [Shah et al., 2022](https://doi.org/10.48048/tis.2022.4642) — separate 316L pit-penetration study, maximum reported 2.4 mm/year at 3 bar H₂S.

**Calculation for aluminum:** `CR[mm/year] = 0.00327 × i_corr[µA/cm²] × EW[g/equiv] / density[g/cm³]`. Both alloys are approximated as aluminum dissolving with valence +3, giving `EW = 26.9815385/3`; densities 6061-T6 = 2.70 and 7075-T6 = 2.81 g/cm³. **These converted rates are not experimentally measured thickness losses.** The electrochemical method and Al³⁺/density simplification can underestimate the consequences of localized corrosion or alloy element behavior.

## Mode 1: uniform experimental benchmark transfer

- Applies **one material-specific published/derived uniform rate** to each mesh face.
- Rate is uniform on all exposed faces; no spatial pit distribution is invented.
- `penetration_i(t) = rate × t_days/365` (constant rate).
- Hypothetical two-sided remaining chamber wall `T = max(0,10 − 2 × penetration)` mm.
- Color reflects one uniform magnitude per material on a shared published benchmark scale; paper conditions differ, so color **does not** give a common H₂S ranking.

## Mode 2: paper-supported baseline + illustrative localized overlay

- Uses **exactly the same five paper-linked base rates** as Mode 1. No low/central/high rates remain in the live viewer.
- Applies the **inherited illustrative spatial hotspot intensity H_i** to each CAD triangle. The hotspot distribution is an assumption and not measured, derived from water pooling physics, electrochemistry, CFD, or mechanical loading.
- The *only literature-based localized corrosion factor* is a 316L **2.4 mm/year deepest-pit rate** in a seven-day experiment, compared with a **0.74 mm/year weight-loss rate** in a separate 316L study. The modeling ratio `F = 2.4 / 0.74 ≈ 3.243243` is **NOT experimentally justified for aluminum, AISI 1020, or AISI 304** and is not a prediction of pit location even for 316L.
- `local_rate_i = material_baseline × [1 + (F−1) × H_i]`, with `H_i∈[0,1]`.
- `penetration_i(t) = local_rate_i × t_days/365`.
- `remaining_10mm_chamber_wall_i = max(0,10 − local_penetration_i − uniform_outer_penetration)` (not exact geometric pairing).
- All five materials share **the same Mode 2 fixed absolute color range**, based on highest literature-derived baseline × F. The viewer labels only the selected alloy's local min/max with two position-accurate ticks; gradient endpoints are unlabeled as requested.
- Color gamma is a visibility enhancement only; it does not change rates.

### Which mode should be used for report conclusions?

**Mode 1** is the strongest presentation of actual published-rate evidence **but not a defensible direct ranking** because experimental conditions differ. **Mode 2** illustrates *sensitivity to hypothetical localized attack* and its consequence for the 10 mm wall, not a validated alloy-specific H₂S prediction. Cite the original papers and all limitations. **If a reviewer requires matched-condition sour-service results, the correct status is *insufficient data*, not a fabricated comparison.**

The 7-day 316L baseline is the nearest match to the chosen original sour reference. For all other materials, even 7-day calculations are transfers from unlike test environments. The 30/90/365-day cases are constant-rate what-if extrapolations, not service-life predictions.

## Reproducible files

- `index.html`: active dual-mode viewer v6.
- `literature_inputs_v6.json`: **single source of truth for all five active rates**, source URLs, original measurements, methods, tested grades and limitations.
- `literature_results_v6.csv`: 40 rows (five materials × two modes × four durations), showing model values and interpretation flags.
- `face_fields.json`: full-surface numerical template and 12,080 face-aligned samples.
- `drum_*.glb`: original assembly geometry.
- `material_scenarios_v4.json`, `research_benchmarks_v5.json`, `simulate_corrosion_v4.py`, and `simulation_results_v4.csv` are **historical records only**. The active v6 website does **not** read the old hypothetical sensitivity file. Do not cite v4 results as active v6 numerical inputs.
