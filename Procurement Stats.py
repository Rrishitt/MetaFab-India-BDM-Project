# ==========================================================
# PROCUREMENT STATISTICS
# MetaFab India BDM Project
# ==========================================================

import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------------------------------------
# SETTINGS
# ----------------------------------------------------------

plt.style.use("ggplot")
sns.set_palette("Set2")

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# LOAD PURCHASE DATA
# ----------------------------------------------------------

purchase = pd.read_excel(
    FILE_PATH,
    sheet_name="PurchaseData"
)

# Convert Date

purchase["Date_of_Purchase"] = pd.to_datetime(
    purchase["Date_of_Purchase"]
)

purchase["Month"] = purchase["Date_of_Purchase"].dt.strftime("%b")

# ----------------------------------------------------------
# BASIC STATISTICS
# ----------------------------------------------------------

print("="*80)
print("PROCUREMENT STATISTICS")
print("="*80)

total_purchase_qty = purchase["Quantity_Purchased_kg"].sum()

total_procurement_cost = purchase["Total_Cost"].sum()

avg_purchase_qty = purchase["Quantity_Purchased_kg"].mean()

median_purchase_qty = purchase["Quantity_Purchased_kg"].median()

std_purchase_qty = purchase["Quantity_Purchased_kg"].std()

material_count = purchase["Material_ID_Item_Name"].nunique()

summary = pd.DataFrame({

    "Metric":[

        "Total Purchase Quantity (kg)",

        "Total Procurement Cost (₹)",

        "Average Purchase Quantity (kg)",

        "Median Purchase Quantity (kg)",

        "Standard Deviation",

        "Number of Raw Materials"

    ],

    "Value":[

        round(total_purchase_qty,2),

        round(total_procurement_cost,2),

        round(avg_purchase_qty,2),

        round(median_purchase_qty,2),

        round(std_purchase_qty,2),

        material_count

    ]

})

print(summary)

summary.to_csv("Procurement_Summary.csv", index=False)

# ----------------------------------------------------------
# MONTHLY PROCUREMENT TREND
# ----------------------------------------------------------

month_order = [

"Jan","Feb","Mar","Apr","May","Jun",

"Jul","Aug","Sep","Oct","Nov","Dec"

]

monthly = (

purchase

.groupby("Month")["Quantity_Purchased_kg"]

.sum()

.reindex(month_order)

.dropna()

)

plt.figure(figsize=(10,5))

plt.plot(

monthly.index,

monthly.values,

marker="o",

linewidth=2

)

plt.title("Monthly Procurement Trend")

plt.xlabel("Month")

plt.ylabel("Quantity Purchased (kg)")

plt.tight_layout()

plt.savefig(

"Fig_4_1_Monthly_Procurement_Trend.png",

dpi=300

)

plt.show()

# ----------------------------------------------------------
# PROCUREMENT BY MATERIAL
# ----------------------------------------------------------

material = (

purchase

.groupby("Material_ID_Item_Name")["Quantity_Purchased_kg"]

.sum()

.sort_values(ascending=False)

)

plt.figure(figsize=(11,6))

sns.barplot(

x=material.values,

y=material.index

)

plt.title("Procurement by Material")

plt.xlabel("Quantity Purchased (kg)")

plt.ylabel("Material")

plt.tight_layout()

plt.savefig(

"Fig_4_2_Procurement_by_Material.png",

dpi=300

)

plt.show()

# ----------------------------------------------------------
# MATERIAL SUMMARY
# ----------------------------------------------------------

material_summary = (

purchase

.groupby("Material_ID_Item_Name")

.agg(

Purchase_Quantity=("Quantity_Purchased_kg","sum"),

Procurement_Cost=("Total_Cost","sum")

)

.sort_values(

"Procurement_Cost",

ascending=False

)

)

print("\n")

print("="*80)

print("MATERIAL-WISE PROCUREMENT")

print("="*80)

print(material_summary)

material_summary.to_csv(

"Material_Procurement_Summary.csv"

)

print("\nAnalysis Completed Successfully.")