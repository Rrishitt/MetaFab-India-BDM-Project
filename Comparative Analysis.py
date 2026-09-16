# ==========================================================
# COMPARATIVE ANALYSIS
# Practical Daily Capacity vs Average Daily Production
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

production = pd.read_excel(
    FILE_PATH,
    sheet_name="ProductionData_6Months"
)

capacity = pd.read_excel(
    FILE_PATH,
    sheet_name="Production_Capacity"
)

# ----------------------------------------------------------
# Average Daily Production by Product
# ----------------------------------------------------------

actual = (
    production
    .groupby("Item_Name")["Good_Units_Produced"]
    .mean()
    .reset_index()
)

actual.columns = [
    "Product",
    "Average Daily Production"
]

# ----------------------------------------------------------
# Merge
# ----------------------------------------------------------

comparison = pd.merge(
    capacity,
    actual,
    on="Product",
    how="left"
)

comparison["Average Daily Production"] = (
    comparison["Average Daily Production"]
    .fillna(0)
)

# ----------------------------------------------------------
# Capacity Utilization
# ----------------------------------------------------------

comparison["Capacity Utilization (%)"] = (
    comparison["Average Daily Production"]
    /
    comparison["Practical Capacity"]
) * 100

comparison["Capacity Gap"] = (
    comparison["Practical Capacity"]
    -
    comparison["Average Daily Production"]
)

print("\n")
print("="*90)
print("DAILY CAPACITY UTILIZATION")
print("="*90)

print(
    comparison.round(2)
)

comparison.to_csv(
    "Capacity_Utilization.csv",
    index=False
)

# ----------------------------------------------------------
# Plot
# ----------------------------------------------------------

x = np.arange(len(comparison))

width = 0.35

plt.figure(figsize=(10,6))

plt.bar(
    x-width/2,
    comparison["Practical Capacity"],
    width,
    label="Practical Daily Capacity"
)

plt.bar(
    x+width/2,
    comparison["Average Daily Production"],
    width,
    label="Average Daily Production"
)

plt.xticks(
    x,
    comparison["Product"],
    rotation=15
)

plt.ylabel("Units / Day")

plt.title(
    "Practical Daily Capacity vs Average Daily Production"
)

# Add value labels
for i, value in enumerate(comparison["Practical Capacity"]):
    plt.text(
        i-width/2,
        value+8,
        f"{value:.0f}",
        ha='center',
        fontsize=9
    )

for i, value in enumerate(comparison["Average Daily Production"]):
    plt.text(
        i+width/2,
        value+8,
        f"{value:.0f}",
        ha='center',
        fontsize=9
    )

plt.legend()

plt.tight_layout()

plt.savefig(
    "Capacity_Comparison.png",
    dpi=300
)

plt.show()

# ----------------------------------------------------------
# Overall Capacity Utilization
# ----------------------------------------------------------

overall_utilization = (
    comparison["Average Daily Production"].sum()
    /
    comparison["Practical Capacity"].sum()
) * 100

print("\n")
print("="*90)
print(f"Overall Daily Capacity Utilization : {overall_utilization:.2f}%")
print("="*90)

# ----------------------------------------------------------
# Best & Worst Utilized Products
# ----------------------------------------------------------

best = comparison.loc[
    comparison["Capacity Utilization (%)"].idxmax()
]

worst = comparison.loc[
    comparison["Capacity Utilization (%)"].idxmin()
]

print("\nHighest Capacity Utilization")
print(best[["Product","Capacity Utilization (%)"]])

print("\nLowest Capacity Utilization")
print(worst[["Product","Capacity Utilization (%)"]])