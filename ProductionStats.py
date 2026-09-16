# ==========================================================
# METAFAB INDIA BDM PROJECT
# DATA LOADING & PREPROCESSING
# ==========================================================

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path

# ----------------------------------------------------------
# Plot Settings
# ----------------------------------------------------------

plt.style.use("ggplot")

plt.rcParams["figure.figsize"] = (10,5)

plt.rcParams["font.size"] = 11

sns.set_palette("Set2")

# ----------------------------------------------------------
# File Path
# ----------------------------------------------------------

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Read Excel Workbook
# ----------------------------------------------------------

xls = pd.ExcelFile(FILE_PATH)

print("="*70)
print("Available Sheets")
print("="*70)

for sheet in xls.sheet_names:
    print(sheet)

print("="*70)

# ----------------------------------------------------------
# Load Required Sheets
# ----------------------------------------------------------

production = pd.read_excel(FILE_PATH,
                           sheet_name="ProductionData_6Months")

# ----------------------------------------------------------
# Convert Date Column
# ----------------------------------------------------------

production["Date"] = pd.to_datetime(
    production["Date"],
    errors="coerce"
)

# ----------------------------------------------------------
# Create Month Column
# ----------------------------------------------------------

production["Month"] = production["Date"].dt.strftime("%b")
# ==========================================================
# 4.2 PRODUCTION STATISTICS
# ==========================================================

print("="*80)
print("PRODUCTION STATISTICS")
print("="*80)

# ----------------------------------------------------------
# Production Summary Statistics
# ----------------------------------------------------------

total_production = production["Good_Units_Produced"].sum()

average_production = production["Good_Units_Produced"].mean()

maximum_production = production["Good_Units_Produced"].max()

minimum_production = production["Good_Units_Produced"].min()

median_production = production["Good_Units_Produced"].median()

std_production = production["Good_Units_Produced"].std()

production_days = production["Date"].nunique()

product_count = production["Item_Name"].nunique()

production_summary = pd.DataFrame({

    "Metric":[

        "Total Good Units Produced",

        "Average Daily Production",

        "Maximum Daily Production",

        "Minimum Daily Production",

        "Median Production",

        "Standard Deviation",

        "Production Days",

        "Products Manufactured"

    ],

    "Value":[

        round(total_production,2),

        round(average_production,2),

        maximum_production,

        minimum_production,

        median_production,

        round(std_production,2),

        production_days,

        product_count

    ]

})

print(production_summary)

production_summary.to_csv(

    "Production_Summary.csv",

    index=False

)

# ----------------------------------------------------------
# Monthly Production Trend
# ----------------------------------------------------------

monthly_production = (

production
.groupby("Month")["Good_Units_Produced"]
.sum()
.reindex(
["Jan","Feb","Mar","Apr","May","Jun",
 "Jul","Aug","Sep","Oct","Nov","Dec"]
)
.dropna()

)

plt.figure(figsize=(11,5))

plt.plot(

    monthly_production.index,

    monthly_production.values,

    marker="o",

    linewidth=2

)

plt.title(

    "Monthly Production Trend",

    fontsize=14,

    weight="bold"

)

plt.xlabel("Month")

plt.ylabel("Good Units Produced")

plt.tight_layout()

plt.savefig(

    "Fig_4_3_Monthly_Production_Trend.png",

    dpi=300,

    bbox_inches="tight"

)

plt.show()

# ----------------------------------------------------------
# Production by Product
# ----------------------------------------------------------

product_production = (

production
.groupby("Item_Name")["Good_Units_Produced"]
.sum()
.sort_values(ascending=False)

)

plt.figure(figsize=(10,6))

sns.barplot(

    x=product_production.values,

    y=product_production.index

)

plt.title(

    "Production by Product",

    fontsize=14,

    weight="bold"

)

plt.xlabel("Units Produced")

plt.ylabel("Product")

plt.tight_layout()

plt.savefig(

    "Fig_4_4_Productwise_Production.png",

    dpi=300,

    bbox_inches="tight"

)

plt.show()

# ----------------------------------------------------------
# Histogram
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

sns.histplot(

    production["Good_Units_Produced"],

    bins=15,

    kde=True

)

plt.title(

    "Distribution of Daily Production",

    fontsize=14,

    weight="bold"

)

plt.xlabel("Good Units Produced")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig(

    "Fig_4_5_Production_Histogram.png",

    dpi=300,

    bbox_inches="tight"

)

plt.show()

# ----------------------------------------------------------
# Daily Production Trend
# ----------------------------------------------------------

daily_production = (

production
.groupby("Date")["Good_Units_Produced"]
.sum()

)

plt.figure(figsize=(12,5))

plt.plot(

    daily_production.index,

    daily_production.values,

    linewidth=1.8

)

plt.title(

    "Daily Production Trend",

    fontsize=14,

    weight="bold"

)

plt.xlabel("Date")

plt.ylabel("Units Produced")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(

    "Fig_4_6_Daily_Production_Trend.png",

    dpi=300,

    bbox_inches="tight"

)

plt.show()

# ----------------------------------------------------------
# Top Performing Products
# ----------------------------------------------------------

print("\n")

print("="*80)

print("TOP PERFORMING PRODUCTS")

print("="*80)

print(product_production)

product_production.to_csv(

    "Productwise_Production.csv"

)

# ----------------------------------------------------------
# Production Variability
# ----------------------------------------------------------

cv = (std_production / average_production) * 100

print("\n")

print("="*80)

print(f"Production Coefficient of Variation : {cv:.2f}%")

print("="*80)

if cv < 10:

    print("Production process is highly stable.")

elif cv < 20:

    print("Production process shows moderate variability.")

else:

    print("Production process exhibits high variability.")

print("\n")

print("="*80)

print("PRODUCTION ANALYSIS COMPLETED")

print("="*80)
