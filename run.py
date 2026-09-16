import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")

# ==========================================================
# FILE PATHS
# ==========================================================

INPUT_FILE = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

OUTPUT_FILE = r"C:\Users\Rishit\OneDrive\Desktop\BDM_Descriptive_Statistics_Report.xlsx"

# ==========================================================
# LOAD EXCEL FILE
# ==========================================================

excel = pd.ExcelFile(INPUT_FILE)

print("=" * 80)
print("Sheets Found")
print("=" * 80)

for s in excel.sheet_names:
    print("•", s)

summary = []

# ==========================================================
# CREATE OUTPUT EXCEL
# ==========================================================

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:

    # ======================================================
    # LOOP THROUGH ALL SHEETS
    # ======================================================

    for sheet in excel.sheet_names:

        print(f"\nProcessing : {sheet}")

        df = pd.read_excel(INPUT_FILE, sheet_name=sheet)

        # Remove blank rows
        df = df.dropna(how="all")

        numeric = df.select_dtypes(include=np.number)
        categorical = df.select_dtypes(exclude=np.number)

        # ==================================================
        # DATASET SUMMARY
        # ==================================================

        dataset_summary = {

            "Dataset": sheet,

            "Rows": len(df),

            "Columns": len(df.columns),

            "Numeric Columns": len(numeric.columns),

            "Categorical Columns": len(categorical.columns),

            "Missing Values": df.isna().sum().sum(),

            "Duplicate Rows": df.duplicated().sum()

        }

        summary.append(dataset_summary)

        # ==================================================
        # NUMERIC DESCRIPTIVE STATISTICS
        # ==================================================

        if len(numeric.columns) > 0:

            stats_df = pd.DataFrame(index=numeric.columns)

            stats_df["Count"] = numeric.count()

            stats_df["Mean"] = numeric.mean()

            stats_df["Median"] = numeric.median()

            stats_df["Mode"] = numeric.mode().iloc[0]

            stats_df["Standard Deviation"] = numeric.std()

            stats_df["Variance"] = numeric.var()

            stats_df["Minimum"] = numeric.min()

            stats_df["25%"] = numeric.quantile(0.25)

            stats_df["50%"] = numeric.quantile(0.50)

            stats_df["75%"] = numeric.quantile(0.75)

            stats_df["Maximum"] = numeric.max()

            stats_df["Range"] = (
                stats_df["Maximum"] -
                stats_df["Minimum"]
            )

            stats_df["IQR"] = (
                stats_df["75%"] -
                stats_df["25%"]
            )

            stats_df["Skewness"] = numeric.skew()

            stats_df["Kurtosis"] = numeric.kurt()

            stats_df = stats_df.round(2)

            sheet_name = sheet[:20] + "_Numeric"

            stats_df.to_excel(writer, sheet_name=sheet_name)

        # ==================================================
        # CATEGORICAL SUMMARY
        # ==================================================

        if len(categorical.columns) > 0:

            cat_summary = []

            for col in categorical.columns:

                mode = categorical[col].mode()

                cat_summary.append({

                    "Variable": col,

                    "Unique Values": categorical[col].nunique(),

                    "Missing Values": categorical[col].isna().sum(),

                    "Most Frequent Value":
                        mode.iloc[0] if len(mode) else "",

                    "Frequency":
                        categorical[col].value_counts().iloc[0]
                        if len(categorical[col].value_counts()) else 0

                })

            cat_summary = pd.DataFrame(cat_summary)

            sheet_name = sheet[:20] + "_Categorical"

            cat_summary.to_excel(
                writer,
                sheet_name=sheet_name,
                index=False
            )

    # ======================================================
    # OVERALL DATASET SUMMARY
    # ======================================================

    summary_df = pd.DataFrame(summary)

    summary_df.to_excel(
        writer,
        sheet_name="Dataset Summary",
        index=False
    )

# ==========================================================
# COMPLETED
# ==========================================================

print("\n" + "=" * 80)
print("DESCRIPTIVE STATISTICS REPORT GENERATED SUCCESSFULLY")
print("=" * 80)

print(f"\nSaved At:\n{OUTPUT_FILE}")

print("=" * 80)