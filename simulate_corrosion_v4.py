#!/usr/bin/env python3
"""Reproduce the 5-grade drum recession sensitivity CSV.
No material-specific H2S electrochemical kinetics, cracking, or FEA is solved.
Run: python3 simulate_corrosion_v4.py
Input: material_scenarios_v4.json and face_fields.json in same directory.
Output: simulated_surface_results_v4_generated.csv
"""
import json
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
profiles = json.loads((ROOT / "material_scenarios_v4.json").read_text())
fields = json.loads((ROOT / "face_fields.json").read_text())
PIT_MULTIPLIER = 2.4 / 0.74  # Measured 316L pit rate / measured 316L average (two studies)
REF_MIN, REF_MAX = 0.7, 2.399351
CASES = ("low", "central", "high")
DAYS = (7, 30, 90, 365)

def local_rate(reference_triangle_rate, baseline_rate):
    # Common illustrative hotspot template; never a predicted pit position.
    intensity = max(0.0, min(1.0, (reference_triangle_rate - REF_MIN) / (REF_MAX - REF_MIN)))
    return baseline_rate * (1.0 + (PIT_MULTIPLIER - 1.0) * intensity)

def integrate_one_day_at_a_time(rate_mm_y, days):
    # Explicit Euler for dh/dt=-corrosion_rate on a non-changing surface.
    recession = 0.0
    for _ in range(days):
        recession += rate_mm_y / 365.0
    return recession

headers = [
    "material", "scenario", "exposure_days", "component",
    "local_min_rate_assumed_mm_per_year", "local_max_rate_assumed_mm_per_year",
    "min_metal_loss_mm", "max_metal_loss_mm",
    "minimum_remaining_chamber_wall_mm_or_na",
    "exposed_area_m2", "scientific_status"
]
out = ROOT / "simulated_surface_results_v4_generated.csv"
with out.open("w", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(headers)
    for m in profiles["materials"].values():
        for scenario in CASES:
            r0 = m[scenario]
            for days in DAYS:
                for name, body in fields["meshes"].items():
                    rates = [local_rate(r, r0) for r in body["rate"]]
                    lo, hi = min(rates), max(rates)
                    stat = fields["partStats"][name]
                    wall = 10.0 - integrate_one_day_at_a_time(hi, days) if name.startswith("chamber_") else "N/A"
                    writer.writerow([
                        m["label"], scenario, days, name,
                        f"{lo:.6f}", f"{hi:.6f}",
                        f"{integrate_one_day_at_a_time(lo, days):.6f}",
                        f"{integrate_one_day_at_a_time(hi, days):.6f}",
                        f"{wall:.6f}" if isinstance(wall, float) else wall,
                        stat["wetArea_m2"],
                        "ENGINEERING_SENSITIVITY_NOT_MATERIAL_SPECIFIC_H2S_MEASUREMENT",
                    ])
print("Wrote", out)
