import pandas as pd
import numpy as np

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# =====================================================
# SHEETS
# =====================================================

sheet_names = [

    "PurchaseData",

    "ProductionData_6Months",

    "Sales_Invoice_6months",

    "RawMaterial_Inventory",

    "FinishedGoods_Inventory",

    "Workers_AttendanceLog",

    "Machine_BreakdownLog"

]

# =====================================================
# DESCRIPTIVE STATISTICS
# =====================================================

for sheet in sheet_names:

    print("\n")
    print("="*90)
    print(sheet.upper())
    print("="*90)

    df = pd.read_excel(FILE_PATH, sheet_name=sheet)

    numeric = df.select_dtypes(include=np.number)

    stats = pd.DataFrame({

        "Mean": numeric.mean(),

        "Median": numeric.median(),

        "Std Dev": numeric.std(),

        "Minimum": numeric.min(),

        "Maximum": numeric.max(),

        "Sum": numeric.sum()

    })

    print(stats.round(2))

    stats.round(2).to_csv(

        f"{sheet}_Summary.csv"

    )

print("\n")
print("="*90)
print("Summary Statistics Generated Successfully")
print("="*90)