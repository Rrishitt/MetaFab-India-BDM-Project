# ==========================================================
# BOTTLENECK & OPERATIONAL INEFFICIENCY ANALYSIS
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

production = pd.read_excel(FILE_PATH,
                           sheet_name="ProductionData_6Months")

breakdown = pd.read_excel(FILE_PATH,
                          sheet_name="Machine_BreakdownLog")

attendance = pd.read_excel(FILE_PATH,
                           sheet_name="Workers_AttendanceLog")

# ----------------------------------------------------------
# Production Loss due to Defects
# ----------------------------------------------------------

good_units = production["Good_Units_Produced"].sum()

defective_units = production["Defective_Units"].sum()

total_units = good_units + defective_units

defect_rate = (defective_units / total_units) * 100

# ----------------------------------------------------------
# Machine Downtime
# ----------------------------------------------------------

total_breakdowns = len(breakdown)

total_downtime = breakdown["Downtime (Hours)"].sum()

avg_downtime = breakdown["Downtime (Hours)"].mean()

# ----------------------------------------------------------
# Labour Availability
# ----------------------------------------------------------

attendance_pct = (

    attendance["Workers Present"].sum()

    /

    attendance["Workers Planned"].sum()

) * 100

# ----------------------------------------------------------
# KPI Table
# ----------------------------------------------------------

kpi = pd.DataFrame({

    "Operational Indicator":[

        "Defect Rate (%)",

        "Total Machine Breakdowns",

        "Total Downtime (Hours)",

        "Average Downtime (Hours)",

        "Worker Attendance (%)"

    ],

    "Value":[

        round(defect_rate,2),

        total_breakdowns,

        round(total_downtime,2),

        round(avg_downtime,2),

        round(attendance_pct,2)

    ]

})

print("\n")
print("="*80)
print("BOTTLENECK ANALYSIS")
print("="*80)

print(kpi)

kpi.to_csv(
    "Operational_Bottlenecks.csv",
    index=False
)

# ----------------------------------------------------------
# Downtime by Machine
# ----------------------------------------------------------

machine = (

breakdown
.groupby("Machine")["Downtime (Hours)"]
.sum()
.sort_values(ascending=False)

)

plt.figure(figsize=(9,5))

machine.plot(kind="bar")

plt.title("Machine-wise Downtime")

plt.xlabel("Machine")

plt.ylabel("Downtime (Hours)")

plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    "Machine_Downtime.png",
    dpi=300
)

plt.show()

# ----------------------------------------------------------
# Print Major Bottleneck
# ----------------------------------------------------------

major_machine = machine.idxmax()

major_hours = machine.max()

print("\n")

print("="*80)

print(f"Major Bottleneck : {major_machine}")

print(f"Downtime : {major_hours:.2f} Hours")

print("="*80)

# ----------------------------------------------------------
# Operational Assessment
# ----------------------------------------------------------

print("\nOperational Assessment")

if defect_rate > 5:
    print("• High defect rate indicates quality losses.")

if attendance_pct < 90:
    print("• Labour availability may affect production continuity.")

if avg_downtime > 2:
    print("• Machine downtime is a significant operational bottleneck.")

if defect_rate <= 5 and attendance_pct >= 90 and avg_downtime <= 2:
    print("• No major operational bottlenecks detected.")