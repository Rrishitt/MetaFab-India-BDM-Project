# ==========================================================
# ROOT CAUSE ANALYSIS
# Data-Driven Prioritization of Operational Issues
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

# ----------------------------------------------------------
# Load Data
# ----------------------------------------------------------

production = pd.read_excel(FILE_PATH,
                           sheet_name="ProductionData_6Months")

attendance = pd.read_excel(FILE_PATH,
                           sheet_name="Workers_AttendanceLog")

breakdown = pd.read_excel(FILE_PATH,
                          sheet_name="Machine_BreakdownLog")

# ----------------------------------------------------------
# Calculate Root Cause Indicators
# ----------------------------------------------------------

defect_rate = (
    production["Defective_Units"].sum()
    /
    (
        production["Good_Units_Produced"].sum()
        +
        production["Defective_Units"].sum()
    )
) * 100

attendance_loss = 100 - (
    attendance["Workers Present"].sum()
    /
    attendance["Workers Planned"].sum()
) * 100

avg_downtime = breakdown["Downtime (Hours)"].mean()

total_breakdowns = len(breakdown)

# ----------------------------------------------------------
# Root Cause Score Table
# ----------------------------------------------------------

root_causes = pd.DataFrame({

    "Potential Root Cause":[

        "Machine Downtime",

        "Production Defects",

        "Labour Absenteeism"

    ],

    "Indicator":[

        round(avg_downtime,2),

        round(defect_rate,2),

        round(attendance_loss,2)

    ],

    "Unit":[

        "Hours",

        "%",

        "%"

    ]

})

root_causes = root_causes.sort_values(
    by="Indicator",
    ascending=False
)

print("\n")
print("="*80)
print("ROOT CAUSE PRIORITIZATION")
print("="*80)

print(root_causes)

root_causes.to_csv(
    "Root_Cause_Prioritization.csv",
    index=False
)

# ----------------------------------------------------------
# Visualization
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

bars = plt.bar(
    root_causes["Potential Root Cause"],
    root_causes["Indicator"]
)

plt.title("Major Operational Root Causes")

plt.ylabel("Indicator Value")

plt.xticks(rotation=10)

for bar in bars:
    plt.text(
        bar.get_x()+bar.get_width()/2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    "Root_Cause_Analysis.png",
    dpi=300
)

plt.show()

# ----------------------------------------------------------
# Identify Primary Root Cause
# ----------------------------------------------------------

primary = root_causes.iloc[0]

print("\n")
print("="*80)
print("PRIMARY ROOT CAUSE")
print("="*80)

print(f"Primary Issue : {primary['Potential Root Cause']}")
print(f"Observed Value: {primary['Indicator']:.2f} {primary['Unit']}")

print("\nPossible Business Implication:")

if primary["Potential Root Cause"] == "Machine Downtime":
    print("- Frequent machine stoppages reduce production continuity.")
    print("- Preventive maintenance should be strengthened.")

elif primary["Potential Root Cause"] == "Production Defects":
    print("- High rejection levels reduce production efficiency.")
    print("- Quality monitoring should be improved.")

else:
    print("- Labour shortage affects production scheduling.")
    print("- Workforce planning should be reviewed.")