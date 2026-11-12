"""Exploratory sales analysis — complements Sales_Analysis_Python.ipynb (stdlib + matplotlib)."""
from __future__ import annotations

import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt

DATA = Path(__file__).resolve().parents[1] / "data" / "sales_raw.csv"
OUT = Path(__file__).resolve().parents[1] / "output"
OUT.mkdir(exist_ok=True)


def load_rows() -> list[dict[str, str]]:
    with DATA.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def enrich(row: dict[str, str]) -> dict[str, float | str]:
    qty = float(row["quantity"])
    price = float(row["unit_price"])
    cost = float(row["unit_cost"])
    disc = float(row["discount_pct"])
    gross = qty * price * (1 - disc / 100)
    total_cost = qty * cost
    profit = gross - total_cost
    margin = (profit / gross * 100) if gross else 0.0
    return {
        "region": row["region"],
        "product_category": row["product_category"],
        "sales_rep": row["sales_rep"],
        "order_date": row["order_date"],
        "gross_sales": gross,
        "profit": profit,
        "profit_margin_pct": margin,
    }


def main() -> None:
    rows = [enrich(r) for r in load_rows()]
    print("Rows:", len(rows))
    print("Total profit:", f"{sum(r['profit'] for r in rows):,.2f}")

    by_region: dict[str, float] = defaultdict(float)
    by_cat: dict[str, float] = defaultdict(float)
    by_rep: dict[str, float] = defaultdict(float)
    by_month: dict[str, float] = defaultdict(float)

    for r in rows:
        by_region[r["region"]] += r["gross_sales"]  # type: ignore
        by_cat[r["product_category"]] += r["profit"]  # type: ignore
        by_rep[r["sales_rep"]] += r["profit"]  # type: ignore
        dt = datetime.fromisoformat(r["order_date"])  # type: ignore
        key = f"{dt.year}-{dt.month:02d}"
        by_month[key] += r["gross_sales"]  # type: ignore

    top_reps = sorted(by_rep.items(), key=lambda x: x[1], reverse=True)[:10]
    months = sorted(by_month.keys())

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    axes[0, 0].bar(by_region.keys(), by_region.values())
    axes[0, 0].set_title("Sales by Region")
    axes[0, 0].tick_params(axis="x", rotation=45)

    axes[0, 1].bar(by_cat.keys(), by_cat.values())
    axes[0, 1].set_title("Profit by Category")
    axes[0, 1].tick_params(axis="x", rotation=45)

    axes[1, 0].bar([x[0] for x in top_reps], [x[1] for x in top_reps])
    axes[1, 0].set_title("Top 10 Reps by Profit")
    axes[1, 0].tick_params(axis="x", rotation=45)

    axes[1, 1].plot(months, [by_month[m] for m in months], marker="o")
    axes[1, 1].set_title("Monthly Revenue Trend")
    axes[1, 1].tick_params(axis="x", rotation=90)

    plt.tight_layout()
    chart_path = OUT / "resume_charts_2x2.png"
    fig.savefig(chart_path, dpi=120)
    print("Wrote", chart_path)

    summary_path = OUT / "analysis_summary.txt"
    best_rep = max(by_rep.items(), key=lambda x: x[1])
    summary_path.write_text(
        "\n".join(
            [
                f"total_sales: {sum(by_region.values()):,.2f}",
                f"total_profit: {sum(r['profit'] for r in rows):,.2f}",
                f"top_rep: {best_rep[0]} (profit {best_rep[1]:,.2f})",
            ]
        ),
        encoding="utf-8",
    )
    print("Wrote", summary_path)


if __name__ == "__main__":
    main()
