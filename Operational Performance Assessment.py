# ==========================================================
# OPERATIONAL PERFORMANCE ASSESSMENT DASHBOARD
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

purchase = pd.read_excel(FILE_PATH, sheet_name="PurchaseData")
production = pd.read_excel(FILE_PATH, sheet_name="ProductionData_6Months")
sales = pd.read_excel(FILE_PATH, sheet_name="Sales_Invoice_6months")
attendance = pd.read_excel(FILE_PATH, sheet_name="Workers_AttendanceLog")
breakdown = pd.read_excel(FILE_PATH, sheet_name="Machine_BreakdownLog")

# ----------------------------------------------------------
# KPIs
# ----------------------------------------------------------

total_procurement_cost = purchase["Total_Cost"].sum()

total_production = production["Good_Units_Produced"].sum()

total_sales = sales["Total Amount (₹)"].sum()

attendance_pct = (
    attendance["Workers Present"].sum()
    /
    attendance["Workers Planned"].sum()
) * 100

defect_rate = (
    production["Defective_Units"].sum()
    /
    (
        production["Good_Units_Produced"].sum()
        +
        production["Defective_Units"].sum()
    )
) * 100

avg_downtime = breakdown["Downtime (Hours)"].mean()

# ----------------------------------------------------------
# Dashboard Table
# ----------------------------------------------------------

dashboard = pd.DataFrame({

    "KPI":[

        "Procurement Cost (₹)",

        "Good Units Produced",

        "Sales Revenue (₹)",

        "Attendance (%)",

        "Defect Rate (%)",

        "Average Downtime (hrs)"

    ],

    "Value":[

        round(total_procurement_cost,2),

        round(total_production,2),

        round(total_sales,2),

        round(attendance_pct,2),

        round(defect_rate,2),

        round(avg_downtime,2)

    ]

})

print("\n")
print("="*80)
print("OPERATIONAL PERFORMANCE DASHBOARD")
print("="*80)

print(dashboard)

dashboard.to_csv(
    "Operational_Dashboard.csv",
    index=False
)

# ----------------------------------------------------------
# Dashboard Chart
# ----------------------------------------------------------

plt.figure(figsize=(10,5))

plt.bar(
    dashboard["KPI"],
    dashboard["Value"]
)

plt.title("Operational Performance Dashboard")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig(
    "Operational_Dashboard.png",
    dpi=300
)

plt.show()

# ----------------------------------------------------------
# Management Summary
# ----------------------------------------------------------

print("\n")
print("="*80)
print("MANAGEMENT SUMMARY")
print("="*80)

if attendance_pct >= 90:
    print("✓ Workforce availability is satisfactory.")
else:
    print("⚠ Workforce attendance requires improvement.")

if defect_rate <= 5:
    print("✓ Product quality is within an acceptable range.")
else:
    print("⚠ High defect rate is affecting production efficiency.")

if avg_downtime <= 2:
    print("✓ Machine downtime is under control.")
else:
    print("⚠ Machine downtime is impacting production planning.")

print("\nOverall operational performance should be interpreted together with")
print("procurement, production, inventory and sales trends to improve")
print("production planning and material flow.")