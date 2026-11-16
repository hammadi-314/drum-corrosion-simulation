# Marine atmospheric corrosion review — external revolver magazine (v7.0)

**Presentation-ready interactive viewer:** https://hammadi-314.github.io/drum-corrosion-simulation/?v=7.0

## Correction to the earlier SA9 report

The six-chamber drum is **outside** the pig launcher and is **not assumed to contact pipeline process fluid**. Earlier SA9 pages 3–5 assumed 60 °C, 3 bar H₂S, 30 bar process pressure, 5 wt% NaCl and 0.5 wt% acetic acid. These were extracted from an internal sour-fluid experimental paper and are **not applicable to the external offshore atmospheric exposure** without evidence of H₂S or process-fluid contact.

Version 7 removes H₂S corrosion predictions and the previous 316L sour-pitting multiplier entirely from the active site. The evaluation now distinguishes chloride / seawater coupons from a marine-geometry inspection-attention map. None of the five paper baselines is an experimentally validated corrosion rate of the actual magazine in offshore service.

## Project exposure — assumed, site conditions to be confirmed

- External offshore platform marine atmosphere, salt deposits, rain/condensation and potential intermittent spray/washdown. **Not process fluid, not sour gas and not intentionally submerged.**
- Primary risks: chloride pitting, galvanic corrosion, wet deposit and crevice corrosion, paint breakdown of carbon steel, inadequate drainage, contamination after washing.
- Metal inside a closed chamber may be sheltered; the viewer shows the full triangulated surface for visualization, **not a measured equal wetting duty**.
- The drum rotates: a low elevation on the parked CAD is not necessarily a permanently water-retaining surface.

## Research-derived numerical chloride/seawater references

| Candidate | Used rate (mm/y) | Paper-derived basis | Experiment | Critical limit |
| --- | ---: | --- | --- | --- |
| Al 6061-T6 | **0.1031524** | 9.47 µA/cm² converted from uncoated coupon polarization | 3.5 wt% NaCl solution; [Materials 2024, Table 3](https://doi.org/10.3390/ma17174285) | Approximate aluminum Faraday conversion, not measured thickness |
| Al 7075-T6 | **0.0032445** | 0.31 µA/cm² converted by same equation | Same 3.5% NaCl paper, same measurement family | Low electrochemical rate does NOT mean pitting-safe offshore or physically superior to 6061 |
| AISI/SAE 1020 (normalization unknown) | **0.1210** | Measured gravimetric weight loss; **0.15 mm/y** separate polarization estimate | **336 h immersion** in 3.5 wt% NaCl, [Sousa et al., ABM 2026](https://doi.org/10.5151/2594-5327-43868) | Bare immersed 1020, not a normalized coated offshore drum |
| AISI 304 | **0.03110** | Published electrochemical rate for flat SS304 after intermittent saline exposure | **168 h intermittent exposure** in 3.5 wt% NaCl; test at **27 °C**, [Metals 2021, Figure 7](https://doi.org/10.3390/met11101543) | One flat sample with its specific exposed surface; not actual outdoor rate |
| AISI 316 candidate | **0.01320** | Published 316L electrochemical rate from unsulfided **298 K control** | Natural seawater at 25 °C **without added sodium sulfide**, [Applied Sciences 2023, Table 5](https://doi.org/10.3390/app13074366) | Grade is 316**L**, not exact 316. Other groups in the paper added sulfide; ONLY the unsulfided 298 K control is used |

For aluminum, `CR(mm/year) ≈ 0.00327 × i_corr(µA/cm²) × EW(g/equiv) / ρ(g/cm³)`, assuming `EW=26.9815385/3` g/equiv and ρ of 2.70 and 2.81 g/cm³ for 6061-T6 and 7075-T6 respectively (ASTM G102-type Faraday conversion). The result is a **uniform-equivalent electrochemical estimate**, not a measured pit depth. Study techniques, test durations and alloy temper verification differ, so comparing the rate magnitudes directly for offshore selection is **not validated**.

## Actual two-mode visualization

### 01. Published chloride benchmarks (quantitative input; not field prediction)

- **One shared color scale** for all five source-specific benchmark rates; each material's entire CAD is a uniform tone. This is deliberate—there is no source-matched spatial pit field.
- Bars are click-to-select and show all five reported/converted benchmark values with their source conditions and units.
- Display fields are baseline corrosion rate (mm/year), illustrative one-face metal recession (mm) or illustrative 10 mm nominal wall remaining after that one-face recession.
- `loss = rate × days / 365`; `remaining_wall = max(0,10−loss)`. The selected 7/30/90/365-day intervals are **constant-rate extrapolations**, not service-life forecasts. A numerical rate estimated by polarization is not the same as 7-day observed penetration. The metal geometry remains unchanged.
- The full CAD is 10 original bodies and 12,080 triangles. The front plate is hidden initially to reveal the chambers but is still included in source area; user can focus on any component, reset camera and save a PNG or CSV.

### 02. Marine wetting attention map (qualitative; not corrosion-rate analysis)

To provide a design-oriented 3D model without fabricating chemistry or pit rates, each triangle is assigned an **inspection-attention index** on a 0–100 visualization scale using a simplified local orientation and elevation heuristic:

```text
u = max(0, world_outward_triangle_normal_z)
low = 1 - clamp((triangle_world_centroid_z-zmin)/(zmax-zmin), 0, 1)
for six chambers:    index = 25 + 45*u + 30*low
for plates and hubs: index = 25 + 45*u + 15*low
```

- The index is **not an ISO 9223 measurement**, corrosion rate, wetted area, true probability, damage depth, CFD result or actual salt deposition estimate.
- The heuristic is used only to highlight surfaces that might warrant checking for salt deposits or retained moisture. Upward-facing surfaces and lower locations are visualized for *inspection attention*.
- Since normal orientation, mounting, rotation, shielding, rain, washdown, geometry of drains, surface roughness and coatings all influence real wetting, no design should conclude that these colors predict actual corrosion zones.
- This map uses **no H₂S sour pitting factor, corrosion multiplier, predicted pit rate or material-specific hotspot kinetics**.

## Standards applicable to the revised exposure

**ISO 9223:2012** — [official ISO publication](https://www.iso.org/standard/53499.html), current edition confirmed in 2022. Classifies the corrosivity of **atmospheres** using standard specimen first-year mass/thickness loss and environmental variables (temperature/humidity/time of wetness, air salinity, pollution). The dashboard compares indicative category **C5** (very high) and **CX** (extreme offshore) as **unconfirmed design reference categories**, not measured categories for this site. Under ISO 9223, typical first-year **standard carbon-steel specimen** thickness-loss category limits are:
- **C5:** more than 80 up to 200 μm/year ≈ **0.08–0.20 mm first year**.
- **CX:** more than 200 up to 700 μm/year ≈ **0.20–0.70 mm first year**.

**Crucial:** These category ranges are *not* extrapolated to aluminum, 304, 316, exact AISI 1020 heat treatment, coated parts, local pit depth or multiple-year wall-thinning; the initial local category requires site exposure/salt/wetness information or specimens (ISO 9226). ISO 9223 explicitly warns first-year rates cannot simply be extrapolated to predict long-term corrosion.

**ISO 12944-2:2017** — [official ISO](https://www.iso.org/standard/64834.html). Classification of environments for steel protective paint systems. **ISO 12944-9:2018** — [official ISO](https://www.iso.org/standard/64832.html). Offshore and related high-durability protective **paint systems for carbon-steel structures**; not a qualification standard for aluminum, stainless alloy components, fasteners or the full uncoated mechanism. A coating specification for 1020 / other steel framing must address actual geometry, prep, paint-system testing and inspection.

## Outputs and reproducibility

- `index.html`: responsive three.js model, tabs, citations, ISO reference cards, live probe, rate bars, screenshot PNG and CSV exports.
- `marine_evidence_v7.json`: canonical active non-H₂S source data, science warnings, standard URLs, formulae and design categories.
- `marine_benchmark_results_v7.csv`: all 5 source rates and hypothetical 7/30/90/365 day one-face results (20 rows).
- `face_fields.json`: **CAD mesh inventory only** in v7. The old sour-rate triangles exist in this historical file but **are not used as corrosion values**.
- `drum_*.glb`: reuses the CAD geometry.
- The old v4/v5/v6 source/input files remain in GitHub for history and **are not loaded by v7**. Their assumed H₂S rates must not be cited in the revised report.

## Presentation conclusions

The external magazine is assessed against **airborne marine salinity / salt wetting**, not a sour-fluid environment. The five literature datasets are **different coupon test conditions** and serve as qualitative/quantitative screening references only. The ISO panel establishes the basis for specifying a coastal/offshore exposure category subject to verification. The 3D qualitative inspection map identifies design features for drainage, washability, dissimilar-metal isolation and corrosion protection—not predicted metal failure. To finalize a candidate, test representative materials/coatings using matched marine atmospheric cycles and evaluate structural FEA and manufacturing as separate decision criteria.
