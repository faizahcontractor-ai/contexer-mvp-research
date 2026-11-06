#!/usr/bin/env python3
"""Generate per-case SVGs from the audited Phase 2 metrics CSV."""
from collections import defaultdict
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "charts"
DATA = ROOT / "metrics.csv"
rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
primary = {}
for row in rows:
    if row["metric"] == "primary_case_outcome":
        primary[(row["case_id"], row["condition"])] = row

cases = sorted({case for case, _ in primary})
colors = {"pass": "#2e7d32", "fail": "#c62828", "not run": "#9e9e9e"}


def svg_text(x, y, value, size=14, weight="normal", color="#222"):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial,sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{color}">{value}</text>'
    )


def status_svg():
    width, row_h, left = 720, 42, 145
    height = 90 + row_h * len(cases)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
    ]
    parts.append(svg_text(20, 28, "Frozen primary outcome by case", 18, "bold"))
    for j, cond in enumerate(["A", "B", "C"]):
        parts.append(svg_text(left + j * 150 + 40, 65, f"Condition {cond}", 14, "bold"))
    for i, case in enumerate(cases):
        y = 82 + i * row_h
        parts.append(svg_text(24, y + 22, case, 14, "bold"))
        for j, cond in enumerate(["A", "B", "C"]):
            row = primary.get((case, cond))
            result = "not run" if not row or row["success"] == "not_measured" else (
                "pass" if row["success"] == "true" else "fail"
            )
            x = left + j * 150
            parts.append(
                f'<rect x="{x}" y="{y}" width="118" height="30" rx="4" fill="{colors[result]}"/>'
            )
            label = {"pass": "PASS", "fail": "FAIL", "not run": "NOT RUN"}[result]
            parts.append(
                svg_text(x + 12, y + 20, label, 12, "bold", "white" if result != "not run" else "#222")
            )
    parts.append(svg_text(24, height - 12, "Per-case only; no pooled effect estimate. C is unmeasured.", 12, "normal", "#555"))
    parts.append("</svg>")
    (OUT / "case-outcomes.svg").write_text("\n".join(parts), encoding="utf-8")


def runs_svg():
    tasks = ["T01", "T02", "T03", "T04"]
    counts = defaultdict(int)
    for row in rows:
        if row["metric"] == "completed_agent_runs" and row["condition"] in {"A", "B", "C"}:
            counts[(row["experiment_id"], row["condition"])] = int(float(row["value"]))
    width, height = 720, 250
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="white"/>',
    ]
    parts.append(svg_text(20, 28, "Completed agent runs by task (saved pilot evidence)", 18, "bold"))
    legend = [("A", "#1565c0"), ("B", "#6a1b9a"), ("C", "#9e9e9e")]
    for j, (cond, color) in enumerate(legend):
        x = 430 + j * 85
        parts.append(f'<rect x="{x}" y="45" width="14" height="14" fill="{color}"/>')
        parts.append(svg_text(x + 20, 57, cond, 12))
    baseline, scale = 195, 48
    for i, task in enumerate(tasks):
        x0 = 160 + i * 135
        parts.append(svg_text(x0 + 18, 220, task, 13, "bold"))
        for j, (cond, color) in enumerate(legend):
            value = counts[(task, cond)]
            x, y = x0 + j * 29, baseline - value * scale
            parts.append(f'<rect x="{x}" y="{y}" width="20" height="{value * scale}" fill="{color}"/>')
            parts.append(svg_text(x + 6, y - 5, str(value), 11))
    parts.append(svg_text(24, 242, "Each A/B task has one completed run; C has zero completed runs.", 12, "normal", "#555"))
    parts.append("</svg>")
    (OUT / "completed-runs.svg").write_text("\n".join(parts), encoding="utf-8")


OUT.mkdir(parents=True, exist_ok=True)
status_svg()
runs_svg()
print("Generated charts/case-outcomes.svg and charts/completed-runs.svg from metrics.csv")
