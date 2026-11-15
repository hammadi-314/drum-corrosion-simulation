# Revolver Drum — Dual-Mode 3D Corrosion Viewer (v5.1)

**Live viewer:** https://hammadi-314.github.io/drum-corrosion-simulation/?v=5

The 3D model comes from the project's six-chamber STEP assembly: **10 CAD bodies**, **12,080 triangular surface faces** and approximately **27.293367 m²** of surface area. Every inside/outside mesh face is considered exposed. No material removal is physically applied to the geometry.

## Two modes — choose from the Analysis mode dropdown

### Mode 1 — published experimental benchmarks (DEFAULT)

Mode 1 uses a distinct **published measurement or transparent published-current-to-rate conversion** for the selected material. The specific source, actually tested material grade, test environment and limitations appear next to the 3D viewer. The five papers **do not share experimental conditions**. **Never treat Mode 1 as a five-alloy corrosion ranking for one H₂S environment.**

Mode 1 assigns the relevant published or converted **UNIFORM benchmark rate to every face** on the drum, because the experimental studies did not measure pit-location fields on the user's CAD. Consequently minimum and maximum rates/penetration are equal for every material. This is intentional and preferable to inventing a spatial failure field. All faces on a selected drum retain a uniform corrosion color, but **the colors now differ across materials** because the visual scale runs from the smallest to the largest reported/derived rate among the five papers. The contrast curve is amplified with `severity = normalized_rate^0.55`; **this changes only appearance, not corrosion rates**. The visual legend therefore shows the shared research-rate range rather than identical endpoints for each material. These paper rates come from different environments and must not be interpreted as a sour-service ranking.

| Candidate dropdown | Sample actually tested | Research original | Site-equivalent corrosion rate | Environmental limitation |
| --- | --- | --- | ---: | --- |
| Al 6061-T6 | Al 6061-T6 | 9.47 µA/cm² corrosion current density | **0.1031524 mm/y** (derived) | 3.5% NaCl, no H₂S |
| Al 7075-T6 | Al 7075-T6 | 0.31 µA/cm² corrosion current density | **0.0032445 mm/y** (derived) | Same chloride paper, no H₂S |
| AISI 1020 normalized candidate | AISI 1020; normalization not specified | 0.58–0.92 mm/y weight-loss range over surface finishes; viewer uses 0.58 smoother condition | **0.580 mm/y** (published) | 25°C, CO₂-saturated 3% NaCl, no H₂S |
| AISI 304 | Uncoated AISI 304 substrate | 0.17 mm/y | **0.170 mm/y** (published) | Simulated H₂S-containing oil/gas field solution; full pressure/temperature unknown in accessible abstract |
| AISI 316 | AISI **316L**, not 316 | 0.74 mm/y | **0.740 mm/y** (316L benchmark proxy) | 60°C, 3 bar H₂S partial / 30 bar total; 5% NaCl, 0.5% acetic acid |

**Aluminum conversion:** Used ASTM G102 / Faraday penetration-rate equation, assuming Al dissolution as Al³⁺, equivalent weight `26.9815385/3 = 8.993846 g/equiv`, approximate density 2.70 g/cm³ for 6061-T6 and 2.81 g/cm³ for 7075-T6:

```text
CR [mm/year] = 0.00327 × i_corr [µA/cm²] × equivalent_weight [g/equiv] / density [g/cm³]
```

These aluminum rate figures are **not reported penetration rates** from the paper and are only uniform-corrosion approximations. Electrochemical corrosion current can fail to capture localized attack. The significant difference between 6061 and 7075 in this NaCl test does **not** prove 7075 is better under H₂S exposure.

**Mode 1 calculation for each face**: `loss_i(t) = published_or_derived_rate × t_days / 365`; hypothetical two-sided chamber-wall thickness `T = max(0, 10 − 2 × loss_i)`. This only transfers coupon data to the model geometry as a numerical illustration; it cannot forecast real drum operation, actual pitting or time to failure. Other components' thickness is marked N/A.

**Mode 1 references:**
- 6061-T6 and 7075-T6: *Effect of Citric Acid Hard Anodizing on the Mechanical Properties and Corrosion Resistance of Different Aluminum Alloys*, 2024, Table 3, uncoated references: https://doi.org/10.3390/ma17174285
- ASTM G102 corrosion-current conversion: https://ecommerce.sist.si/catalog/standards/astm/6fd59c55-07d4-42ad-8512-bfc5f750a993/astm-g102-23
- AISI 1020 (CO₂, **not** H₂S): Mohammed et al., 2026: https://doi.org/10.18280/ijdne.210410
- AISI 304 (H₂S simulated oil/gas field, missing full test conditions): Huang et al., 2023: https://doi.org/10.1007/s12666-023-02986-2
- AISI 316L (sour reference, **not** exact 316): Shah et al., 2020: https://pmc.ncbi.nlm.nih.gov/articles/PMC7399776/

### Mode 2 — common-condition sour-service numerical SENSITIVITY

Retains the previous common **60°C, 3 bar H₂S partial pressure, 30 bar total, 5 wt% NaCl and 0.5 wt% acetic acid** scenario. The five material-specific low/central/high rate values in `material_scenarios_v4.json` are **unvalidated engineering sensitivity assumptions**, not measurements from experiments under matched conditions.

For each face `i`, previous illustrative hotspot reference value `R_i`, and base rate `r_m`:

```text
hotspot_i = clamp((R_i − 0.700) / (2.399351 − 0.700), 0, 1)
common_rate_multiplier = 2.4 / 0.74 = 3.243243 (316L literature comparison)
local_rate_i = r_m × [1 + (common_rate_multiplier − 1) × hotspot_i]
loss_i(t + 1 day) = loss_i(t) + local_rate_i / 365
remaining_chamber_wall = max(0, 10 − local_inner_loss − outer_baseline_loss)
```

All inner and outer surfaces are exposed. The hottest spatial locations are **assumed**, not predicted by physics. The common factor is illustrative and not validated for aluminum, 1020, 304 or 316. The two-sided wall assumption does not geometrically pair surfaces; it simply subtracts an assumed local interior loss and opposite exterior uniform baseline.

### Common UI and numerical limitations

- Material, part, exposure interval (7, 30, 90, 365 days), output field (rate, loss, remaining wall), orbit/zoom, click-to-probe, and export CSV work in **both modes**.
- In **Mode 1**, the low/central/high selector is hidden because laboratory benchmark results are not three arbitrary scenarios. In **Mode 2**, it remains available.
- **Mode 1:** Colors are mapped to one shared rate range across the five different published study benchmarks, with a stronger visual contrast (`gamma 0.55`). Each material is still uniformly colored across its entire CAD surface, because the source does not establish drum-specific hotspots. These colors do **not** establish comparative resistance to identical H₂S conditions.
- **Mode 2:** Numerical values and illustrative hotspot locations are unchanged. The displayed severity is a perceptual blend of **72% within-material hotspot-normalized intensity** and **28% cross-material assumed-rate-normalized intensity**, raised to exponent `0.85` for visibility. The selected material's legend uses the same visual mapping, ensuring colors and legend match. This is a display choice, not a new physical material-corrosion model.
- For remaining chamber wall, the left (cool-color) legend endpoint denotes **higher thickness** and the right (warm-color) endpoint denotes **lower thickness**. Gray end plates and hubs have no evaluated thickness but remain exposed.
- The **five-material table in Mode 1 is descriptive only**; different temperatures, H₂S concentration, salinity, sample finish/grades and methods prevent a quantitative same-condition ranking.
- `Export readings CSV` includes mode, tested grade, research URL, experiment environment, calculated loss and limitations for all 10 components.
- Time integration assumes a **constant corrosion rate**, so 30/90/365-day scenarios are mathematically linear extrapolations, not verified service-life estimates.
- Neither mode performs electrochemical FEM, sour-service cracking analysis, CFD, geometric erosion, structural pressure calculations or ISO 15156 qualification.

## Files and reproducibility

- `index.html` — dual-mode interactive 3D website
- `research_benchmarks_v5.json` — **Mode 1** source measurements, conversions, conditions, applicability limitations
- `research_mode1_results_v5.csv` — **Mode 1** reproduction of 5 × 4 exposure-duration uniform benchmarks
- `material_scenarios_v4.json` — **Mode 2** hypothetical low/central/high inputs and bibliography
- `simulate_corrosion_v4.py` — Mode 2 computational reproduction
- `simulation_results_v4.csv` — Mode 2 60-case summary
- `face_fields.json` — exposure and prior illustrative hotspot template, 12,080 triangle samples
- `drum_*.glb` — geometry used for all five material selections

## Senior-design progression

The update separates **actual published evidence** from **engineering assumptions**. Mode 1 documents where the present literature does and does not match your selected sour-service conditions; Mode 2 tests the sensitivity of wall-thinning results to plausible-but-unvalidated numerical inputs. Together these tools support the requirement for qualified sour-service materials, corrosion-protection design, and targeted laboratory testing and structural FEA. **Neither mode supports final selection of an alloy on corrosion alone.**
