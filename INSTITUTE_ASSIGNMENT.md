# Cloud Vision Technologies — graded sales assignment

**Dataset:** https://www.kaggle.com/datasets/vinothkannaece/sales-dataset (`sales_data.csv`)  
**Submission:** Push Python notebook/code to GitHub and share repo link (due **08-09-2026** per institute message).

| Part | Tasks | Deliverable in this repo |
|------|-------|---------------------------|
| **A – Excel** | 1–4 cleaning, calculated columns, date/category, pivots | [sales-data-analysis](https://github.com/Deekshith254/sales-data-analysis) — `Sales_Data_Analysis.xlsx`, `docs/EXCEL_STEPS.md` |
| **B – Pandas** | 5–8 inspection, filters, profit columns, groupby rep | `Sales_Analysis_Python.ipynb` |
| **C – Matplotlib** | 9–12 bar charts (region, category, rep), monthly line | Same notebook + `src/sales_eda.py` charts |

## Task mapping (institute wording)

**Part A — Excel**

1. Clean data (duplicates, missing, formats) — document findings  
2. Calculated columns: profit & cost from `Unit_Cost`, `Unit_Price`, `Quantity_Sold`  
3. Year, month, sales category from date & amount  
4. Pivot tables: Region, Product_Category, Sales_Rep, Customer_Type  

**Part B — Pandas**

5. Load CSV — shape, dtypes, stats, missing, duplicates  
6. Multi-condition filters (`Sales_Amount`, `Region`, `Product_Category`, `Customer_Type`)  
7. Profit Per Unit, Total Cost, Profit — highest profit category  
8. `groupby` summary by `Sales_Rep`  

**Part C — Matplotlib**

9. Bar — total sales by Region  
10. Bar — sales by Product_Category  
11. Bar — sales by Sales_Rep  
12. Line — monthly sales trend  

Work should be **your own** (institute: no ChatGPT/Claude for writing code; concept help only).
