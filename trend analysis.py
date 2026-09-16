# ==========================================================
# TREND ANALYSIS
# Procurement vs Production vs Sales
# Analysis Period: January 2026 - June 2026
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

purchase = pd.read_excel(
    FILE_PATH,
    sheet_name="PurchaseData"
)

production = pd.read_excel(
    FILE_PATH,
    sheet_name="ProductionData_6Months"
)

sales = pd.read_excel(
    FILE_PATH,
    sheet_name="Sales_Invoice_6months"
)

# ----------------------------------------------------------
# Convert Date Columns
# ----------------------------------------------------------

purchase["Date_of_Purchase"] = pd.to_datetime(
    purchase["Date_of_Purchase"],
    dayfirst=True,
    errors="coerce"
)

production["Date"] = pd.to_datetime(
    production["Date"],
    dayfirst=True,
    errors="coerce"
)

sales["Date"] = pd.to_datetime(
    sales["Date"],
    dayfirst=True,
    errors="coerce"
)

# ----------------------------------------------------------
# Check Invalid Dates
# ----------------------------------------------------------

print("=" * 80)
print("INVALID DATE CHECK")
print("=" * 80)

print("Purchase   :", purchase["Date_of_Purchase"].isna().sum())
print("Production :", production["Date"].isna().sum())
print("Sales      :", sales["Date"].isna().sum())

# Remove rows with invalid dates
purchase = purchase.dropna(
    subset=["Date_of_Purchase"]
)

production = production.dropna(
    subset=["Date"]
)

sales = sales.dropna(
    subset=["Date"]
)

# ----------------------------------------------------------
# Create Month Column
# ----------------------------------------------------------

purchase["Month"] = purchase["Date_of_Purchase"].dt.to_period("M")

production["Month"] = production["Date"].dt.to_period("M")

sales["Month"] = sales["Date"].dt.to_period("M")

# ----------------------------------------------------------
# DEFINE ANALYSIS PERIOD
# January 2026 to June 2026
# ----------------------------------------------------------

START_MONTH = pd.Period("2026-01", freq="M")
END_MONTH = pd.Period("2026-06", freq="M")

# Filter all datasets to the required period

purchase = purchase[
    (purchase["Month"] >= START_MONTH) &
    (purchase["Month"] <= END_MONTH)
]

production = production[
    (production["Month"] >= START_MONTH) &
    (production["Month"] <= END_MONTH)
]

sales = sales[
    (sales["Month"] >= START_MONTH) &
    (sales["Month"] <= END_MONTH)
]

# ----------------------------------------------------------
# Monthly Aggregation
# ----------------------------------------------------------

monthly_purchase = (
    purchase
    .groupby("Month")["Quantity_Purchased_kg"]
    .sum()
)

monthly_production = (
    production
    .groupby("Month")["Good_Units_Produced"]
    .sum()
)

monthly_sales = (
    sales
    .groupby("Month")["Total Amount (₹)"]
    .sum()
)

# ----------------------------------------------------------
# Create COMPLETE Jan-Jun Month Index
# ----------------------------------------------------------

month_index = pd.period_range(
    start=START_MONTH,
    end=END_MONTH,
    freq="M"
)

# ----------------------------------------------------------
# Merge Monthly Data
# ----------------------------------------------------------

trend = pd.DataFrame(index=month_index)

trend["Purchase (kg)"] = monthly_purchase
trend["Production (Units)"] = monthly_production
trend["Sales Revenue (₹)"] = monthly_sales

# Replace missing months with 0
trend = trend.fillna(0)

# Make sure months are in chronological order
trend = trend.sort_index()

# ----------------------------------------------------------
# Display Table
# ----------------------------------------------------------

print("\n")
print("=" * 80)
print("MONTHLY TREND TABLE")
print("=" * 80)

print(trend)

# Save table
trend.to_csv(
    "Monthly_Trend_Table.csv",
    index=True
)

# ----------------------------------------------------------
# Convert PeriodIndex to String ONLY FOR PLOTTING
# ----------------------------------------------------------

plot_trend = trend.copy()

plot_trend.index = plot_trend.index.astype(str)

# ----------------------------------------------------------
# Plot 1
# Procurement vs Production
# ----------------------------------------------------------

plt.figure(figsize=(11, 5))

plt.plot(
    plot_trend.index,
    plot_trend["Purchase (kg)"],
    marker="o",
    linewidth=2,
    label="Purchase"
)

plt.plot(
    plot_trend.index,
    plot_trend["Production (Units)"],
    marker="s",
    linewidth=2,
    label="Production"
)

plt.title("Monthly Procurement vs Production")
plt.xlabel("Month")
plt.ylabel("Quantity")

plt.xticks(rotation=45)

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig(
    "Trend_Procurement_vs_Production.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ----------------------------------------------------------
# Plot 2
# Monthly Sales Revenue
# ----------------------------------------------------------

plt.figure(figsize=(11, 5))

plt.plot(
    plot_trend.index,
    plot_trend["Sales Revenue (₹)"],
    marker="D",
    linewidth=2,
    color="green"
)

plt.title("Monthly Sales Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "Trend_Sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("\nTrend analysis completed successfully.")
print("Analysis period: January 2026 to June 2026")