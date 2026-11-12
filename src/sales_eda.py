"""Matplotlib charts for institute assignment Part C (tasks 9–12)."""
from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

DATA = Path(__file__).resolve().parents[1] / "data" / "sales_data.csv"
OUT = Path(__file__).resolve().parents[1] / "output"
OUT.mkdir(exist_ok=True)


def load_rows() -> list[dict[str, str]]:
    with DATA.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> None:
    rows = load_rows()
    by_region: dict[str, float] = defaultdict(float)
    by_cat: dict[str, float] = defaultdict(float)
    by_rep: dict[str, float] = defaultdict(float)
    by_month: dict[str, float] = defaultdict(float)

    for r in rows:
        amt = float(r["Sales_Amount"])
        by_region[r["Region"]] += amt
        by_cat[r["Product_Category"]] += amt
        by_rep[r["Sales_Rep"]] += amt
        dt = datetime.fromisoformat(r["Sale_Date"])
        by_month[f"{dt.year}-{dt.month:02d}"] += amt

    months = sorted(by_month.keys())

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Sales analysis — Kaggle sales_data (Part C)", fontsize=13)

    axes[0, 0].bar(by_region.keys(), by_region.values())
    axes[0, 0].set_title("9. Total sales by Region")
    axes[0, 0].tick_params(axis="x", rotation=45)

    axes[0, 1].bar(by_cat.keys(), by_cat.values())
    axes[0, 1].set_title("10. Total sales by Product Category")
    axes[0, 1].tick_params(axis="x", rotation=45)

    axes[1, 0].bar(by_rep.keys(), by_rep.values())
    axes[1, 0].set_title("11. Total sales by Sales Rep")
    axes[1, 0].tick_params(axis="x", rotation=45)

    axes[1, 1].plot(months, [by_month[m] for m in months], marker="o")
    axes[1, 1].set_title("12. Monthly sales trend")
    axes[1, 1].tick_params(axis="x", rotation=90)

    plt.tight_layout()
    out = OUT / "part_c_charts_2x2.png"
    fig.savefig(out, dpi=120)
    print("Wrote", out, "| rows:", len(rows))


if __name__ == "__main__":
    main()
