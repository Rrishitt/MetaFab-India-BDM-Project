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

purchase = pd.read_excel(FILE_PATH,
                         sheet_name="PurchaseData")

production = pd.read_excel(FILE_PATH,
                           sheet_name="ProductionData_6Months")

sales = pd.read_excel(FILE_PATH,
                      sheet_name="Sales_Invoice_6months")

raw_inventory = pd.read_excel(FILE_PATH,
                              sheet_name="RawMaterial_Inventory")

finished_inventory = pd.read_excel(FILE_PATH,
                                   sheet_name="FinishedGoods_Inventory")

attendance = pd.read_excel(FILE_PATH,
                           sheet_name="Workers_AttendanceLog")

breakdown = pd.read_excel(FILE_PATH,
                          sheet_name="Machine_BreakdownLog")

capacity = pd.read_excel(FILE_PATH,
                         sheet_name="Production_Capacity")

# ----------------------------------------------------------
# Convert Date Columns
# ----------------------------------------------------------

datasets = [
    purchase,
    production,
    sales,
    raw_inventory,
    finished_inventory,
    attendance,
    breakdown
]

for df in datasets:

    for col in df.columns:

        if "date" in col.lower():

            df[col] = pd.to_datetime(
                df[col],
                errors="coerce"
            )


# ----------------------------------------------------------
# Dataset Shapes
# ----------------------------------------------------------

print("\n")

print("="*70)
print("DATASET SHAPES")
print("="*70)

for name, df in zip(
[
"Purchase",
"Production",
"Sales",
"Raw Inventory",
"Finished Inventory",
"Attendance",
"Breakdown"
],
datasets):

    print(f"{name:<20}: {df.shape}")

# ----------------------------------------------------------
# Create Month Column
# ----------------------------------------------------------

for df in datasets:

    for col in df.columns:

        if "date" in col.lower():

            df["Month"] = df[col].dt.strftime("%b")

            break

print("\n")

print("="*70)
print("DATA LOADED SUCCESSFULLY")
print("="*70)

