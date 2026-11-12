"""Exploratory sales analysis — complements Sales_Analysis_Python.ipynb."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

DATA = Path(__file__).resolve().parents[1] / "data" / "sales_raw.csv"
OUT = Path(__file__).resolve().parents[1] / "output"
OUT.mkdir(exist_ok=True)


def load() -> pd.DataFrame:
    df = pd.read_csv(DATA, parse_dates=["order_date"])
    df["gross_sales"] = df["quantity"] * df["unit_price"] * (1 - df["discount_pct"] / 100)
    df["total_cost"] = df["quantity"] * df["unit_cost"]
    df["profit"] = df["gross_sales"] - df["total_cost"]
    df["profit_margin_pct"] = (df["profit"] / df["gross_sales"].replace(0, pd.NA)) * 100
    return df


def main() -> None:
    df = load()
    print("Rows:", len(df))
    print("Total profit:", f"{df['profit'].sum():,.2f}")
    print("\nTop regions by profit:\n", df.groupby("region")["profit"].sum().sort_values(ascending=False))

    by_month = df.groupby(df["order_date"].dt.to_period("M"))["gross_sales"].sum()
    by_month.index = by_month.index.astype(str)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    df.groupby("region")["profit"].sum().plot(kind="bar", ax=axes[0], title="Profit by Region")
    by_month.plot(kind="line", ax=axes[1], title="Monthly Revenue Trend", marker="o")
    plt.tight_layout()
    fig.savefig(OUT / "sales_summary.png", dpi=120)
    print("Wrote", OUT / "sales_summary.png")


if __name__ == "__main__":
    main()
