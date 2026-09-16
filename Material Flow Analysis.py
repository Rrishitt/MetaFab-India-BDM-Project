# ==========================================================
# MATERIAL FLOW ANALYSIS
# Procurement → Production → Sales
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Read Data
# ----------------------------------------------------------

purchase = pd.read_excel(FILE_PATH, sheet_name="PurchaseData")
production = pd.read_excel(FILE_PATH, sheet_name="ProductionData_6Months")
sales = pd.read_excel(FILE_PATH, sheet_name="Sales_Invoice_6months")

# ----------------------------------------------------------
# Convert Dates
# ----------------------------------------------------------

purchase["Date_of_Purchase"] = pd.to_datetime(
    purchase["Date_of_Purchase"],
    errors="coerce"
)

production["Date"] = pd.to_datetime(
    production["Date"],
    errors="coerce"
)

sales["Date"] = pd.to_datetime(
    sales["Date"],
    errors="coerce"
)

purchase["Month"] = purchase["Date_of_Purchase"].dt.strftime("%b")
production["Month"] = production["Date"].dt.strftime("%b")
sales["Month"] = sales["Date"].dt.strftime("%b")

month_order = ["Jan","Feb","Mar","Apr","May","Jun"]

# ----------------------------------------------------------
# Monthly Aggregation
# ----------------------------------------------------------

procurement = (
    purchase.groupby("Month")["Quantity_Purchased_kg"]
    .sum()
    .reindex(month_order)
)

production_qty = (
    production.groupby("Month")["Good_Units_Produced"]
    .sum()
    .reindex(month_order)
)

sales_qty = (
    sales.groupby("Month")["Quantity Sold"]
    .sum()
    .reindex(month_order)
)

material_flow = pd.DataFrame({

    "Procurement (kg)": procurement,
    "Production (Units)": production_qty,
    "Sales (Units)": sales_qty

}).dropna(how="all")

print("\n")
print("="*70)
print("MATERIAL FLOW SUMMARY")
print("="*70)
print(material_flow)

material_flow.to_csv(
    "Material_Flow_Summary.csv"
)

# ----------------------------------------------------------
# Material Flow Trend
# ----------------------------------------------------------

plt.figure(figsize=(12,6))

plt.plot(
    material_flow.index,
    material_flow["Procurement (kg)"],
    marker="o",
    linewidth=2,
    label="Procurement"
)

plt.plot(
    material_flow.index,
    material_flow["Production (Units)"],
    marker="s",
    linewidth=2,
    label="Production"
)

plt.plot(
    material_flow.index,
    material_flow["Sales (Units)"],
    marker="^",
    linewidth=2,
    label="Sales"
)

plt.title(
    "Material Flow Across Procurement, Production and Sales",
    fontsize=14,
    weight="bold"
)

plt.xlabel("Month")
plt.ylabel("Quantity")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Material_Flow_Analysis.png",
    dpi=300
)

plt.show()

print("\nFigure saved as : Material_Flow_Analysis.png")