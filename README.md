# Sales Performance & Profitability Analysis (Python)

**Author:** Salimeda Deekshith  
**Tools:** Python, Pandas, NumPy, Matplotlib, Jupyter

Exploratory analysis and visualizations for the same sales domain as the Excel workbook in [sales-data-analysis](https://github.com/Deekshith254/sales-data-analysis).

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
pip install -r requirements.txt
python src/sales_eda.py
jupyter notebook Sales_Analysis_Python.ipynb
```

## Repository layout

| Path | Description |
|------|-------------|
| `Sales_Analysis_Python.ipynb` | Full exploratory workflow with charts |
| `src/sales_eda.py` | Scriptable EDA: margins, groupbys, bar/line plots |
| `data/sales_raw.csv` | Synthetic transactional sample (regenerate from parent `scripts/generate_datasets.py`) |

## Resume highlights covered

- `groupby()` aggregations for sales, profit margins, and rep performance  
- Multi-condition filtering and representative performance rankings  
- Matplotlib **bar** and **line** charts by region, category, rep, and month  

## License

MIT
