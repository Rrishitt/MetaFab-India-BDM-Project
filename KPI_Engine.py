# ==========================================================
# MODULE 5.1A
# KPI ENGINE - CORE FOUNDATION
#
# Project:
# Improving Production Planning through Material Flow Analysis
# ==========================================================

import os
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

# ==========================================================
# PATHS
# ==========================================================

INPUT_FILE = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab Mastersheet.xlsx"

OUTPUT_FOLDER = r"C:\Users\Rishit\OneDrive\Desktop\MetaFab_Output"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("="*80)
print("MetaFab KPI Engine")
print("="*80)

# ==========================================================
# LOAD EXCEL
# ==========================================================

excel = pd.ExcelFile(INPUT_FILE)

print("\nSheets Detected\n")

for sheet in excel.sheet_names:
    print("•", sheet)

# ==========================================================
# LOAD ALL SHEETS
# ==========================================================

datasets = {}

for sheet in excel.sheet_names:

    df = pd.read_excel(INPUT_FILE, sheet_name=sheet)

    df = df.dropna(how="all")

    datasets[sheet] = df

print("\nTotal Sheets Loaded :", len(datasets))

# ==========================================================
# CLEAN COLUMN NAMES
# ==========================================================

def clean_columns(df):

    df.columns = (
        df.columns
        .astype(str)
        .str.strip()
        .str.replace("\n"," ")
        .str.replace("_"," ")
        .str.replace("-"," ")
        .str.replace("  "," ")
    )

    return df

for key in datasets:

    datasets[key] = clean_columns(datasets[key])

# ==========================================================
# COLUMN DETECTOR
# ==========================================================

def detect_column(df, keywords):

    cols = list(df.columns)

    for key in keywords:

        for col in cols:

            if key.lower() in col.lower():

                return col

    return None

# ==========================================================
# DETECT IMPORTANT COLUMNS
# ==========================================================

def detect_all_columns(df):

    detected = {}

    detected["date"] = detect_column(df,
        ["date","day","invoice"])

    detected["quantity"] = detect_column(df,
        ["qty","quantity","units","purchased","sold"])

    detected["amount"] = detect_column(df,
        ["amount","cost","value","price","total"])

    detected["product"] = detect_column(df,
        ["product","item","material"])

    detected["customer"] = detect_column(df,
        ["customer","client"])

    detected["supplier"] = detect_column(df,
        ["supplier","vendor"])

    detected["machine"] = detect_column(df,
        ["machine"])

    detected["downtime"] = detect_column(df,
        ["downtime","hours"])

    detected["attendance"] = detect_column(df,
        ["present","attendance","workers"])

    detected["opening"] = detect_column(df,
        ["opening"])

    detected["closing"] = detect_column(df,
        ["closing"])

    detected["consumed"] = detect_column(df,
        ["consumed","usage"])

    detected["capacity"] = detect_column(df,
        ["capacity"])

    detected["defect"] = detect_column(df,
        ["defect","rejected","rework"])

    return detected

# ==========================================================
# DATASET PROFILE
# ==========================================================

def dataset_profile(df):

    profile = {}

    profile["Rows"] = len(df)

    profile["Columns"] = len(df.columns)

    profile["Numeric Columns"] = len(
        df.select_dtypes(include=np.number).columns
    )

    profile["Categorical Columns"] = len(
        df.select_dtypes(exclude=np.number).columns
    )

    profile["Missing Values"] = int(
        df.isna().sum().sum()
    )

    profile["Duplicate Rows"] = int(
        df.duplicated().sum()
    )

    profile["Memory (KB)"] = round(
        df.memory_usage(deep=True).sum()/1024,
        2
    )

    return profile

# ==========================================================
# DATA QUALITY SCORE
# ==========================================================

def quality_score(df):

    rows = len(df)

    if rows == 0:

        return 0

    missing = df.isna().sum().sum()

    duplicate = df.duplicated().sum()

    cells = rows * len(df.columns)

    missing_ratio = missing / cells

    duplicate_ratio = duplicate / rows

    score = (
        100
        - missing_ratio*50
        - duplicate_ratio*50
    )

    score = max(score,0)

    return round(score,2)

# ==========================================================
# BUSINESS HEALTH
# ==========================================================

def health_flag(score):

    if score >= 95:

        return "Excellent"

    elif score >= 90:

        return "Good"

    elif score >= 80:

        return "Fair"

    elif score >= 70:

        return "Needs Attention"

    else:

        return "Critical"

# ==========================================================
# PROFILE EVERY DATASET
# ==========================================================

profiles = []

print("\n")
print("="*80)
print("Dataset Profiles")
print("="*80)

for name,df in datasets.items():

    profile = dataset_profile(df)

    detected = detect_all_columns(df)

    profile["Dataset"] = name

    profile["Quality Score"] = quality_score(df)

    profile["Health"] = health_flag(
        profile["Quality Score"]
    )

    profile["Detected Date"] = detected["date"]

    profile["Detected Quantity"] = detected["quantity"]

    profile["Detected Amount"] = detected["amount"]

    profile["Detected Product"] = detected["product"]

    profile["Detected Customer"] = detected["customer"]

    profile["Detected Supplier"] = detected["supplier"]

    profiles.append(profile)

    print("\n",name)

    print("-"*60)

    for k,v in profile.items():

        print(f"{k:25}: {v}")

# ==========================================================
# SAVE PROFILE
# ==========================================================

profile_df = pd.DataFrame(profiles)

profile_path = os.path.join(
    OUTPUT_FOLDER,
    "Dataset_Profile.csv"
)

profile_df.to_csv(
    profile_path,
    index=False
)

print("\n")
print("="*80)
print("Dataset Profile Saved")
print(profile_path)
print("="*80)

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def safe_sum(df,col):

    if col is None:

        return np.nan

    return pd.to_numeric(
        df[col],
        errors="coerce"
    ).sum()

def safe_mean(df,col):

    if col is None:

        return np.nan

    return pd.to_numeric(
        df[col],
        errors="coerce"
    ).mean()

def safe_std(df,col):

    if col is None:

        return np.nan

    return pd.to_numeric(
        df[col],
        errors="coerce"
    ).std()

def safe_max(df,col):

    if col is None:

        return np.nan

    return pd.to_numeric(
        df[col],
        errors="coerce"
    ).max()

def safe_min(df,col):

    if col is None:

        return np.nan

    return pd.to_numeric(
        df[col],
        errors="coerce"
    ).min()

def safe_unique(df,col):

    if col is None:

        return 0

    return df[col].nunique()

print("\nCore Engine Loaded Successfully.")
print("Ready for KPI Calculations (Module 5.1B)")

# ==========================================================
# MODULE 5.1B
# BUSINESS KPI CALCULATION ENGINE
# ==========================================================

print("\n")
print("="*80)
print("BUSINESS KPI ENGINE")
print("="*80)

# ----------------------------------------------------------
# KPI STORAGE
# ----------------------------------------------------------

all_kpis = {}

# ----------------------------------------------------------
# GENERIC KPI FUNCTION
# ----------------------------------------------------------

def generic_kpis(df):

    numeric = df.select_dtypes(include=np.number)

    result = {}

    result["Total Records"] = len(df)

    result["Total Columns"] = len(df.columns)

    result["Numeric Columns"] = len(numeric.columns)

    result["Categorical Columns"] = len(df.columns)-len(numeric.columns)

    result["Missing Values"] = int(df.isna().sum().sum())

    result["Duplicate Rows"] = int(df.duplicated().sum())

    result["Data Quality Score"] = quality_score(df)

    return result

# ----------------------------------------------------------
# PURCHASE KPI
# ----------------------------------------------------------

def purchase_kpis(df):

    detect = detect_all_columns(df)

    qty = detect["quantity"]

    amt = detect["amount"]

    supplier = detect["supplier"]

    product = detect["product"]

    kpi = generic_kpis(df)

    if qty:

        series = pd.to_numeric(df[qty],errors="coerce")

        kpi["Total Purchase Quantity"] = round(series.sum(),2)

        kpi["Average Purchase Quantity"] = round(series.mean(),2)

        kpi["Median Purchase Quantity"] = round(series.median(),2)

        kpi["Maximum Purchase"] = round(series.max(),2)

        kpi["Minimum Purchase"] = round(series.min(),2)

        kpi["Purchase Std Dev"] = round(series.std(),2)

    if amt:

        money = pd.to_numeric(df[amt],errors="coerce")

        kpi["Total Procurement Cost"] = round(money.sum(),2)

        kpi["Average Procurement Cost"] = round(money.mean(),2)

        kpi["Highest Procurement Cost"] = round(money.max(),2)

        kpi["Lowest Procurement Cost"] = round(money.min(),2)

    if supplier:

        kpi["Unique Suppliers"] = df[supplier].nunique()

    if product:

        kpi["Unique Materials"] = df[product].nunique()

    return kpi

# ----------------------------------------------------------
# SALES KPI
# ----------------------------------------------------------

def sales_kpis(df):

    detect = detect_all_columns(df)

    qty = detect["quantity"]

    amount = detect["amount"]

    customer = detect["customer"]

    product = detect["product"]

    kpi = generic_kpis(df)

    if qty:

        s = pd.to_numeric(df[qty],errors="coerce")

        kpi["Total Quantity Sold"] = round(s.sum(),2)

        kpi["Average Quantity Sold"] = round(s.mean(),2)

        kpi["Median Quantity Sold"] = round(s.median(),2)

        kpi["Largest Sales Order"] = round(s.max(),2)

    if amount:

        a = pd.to_numeric(df[amount],errors="coerce")

        kpi["Total Revenue"] = round(a.sum(),2)

        kpi["Average Invoice Value"] = round(a.mean(),2)

        kpi["Maximum Invoice"] = round(a.max(),2)

        kpi["Minimum Invoice"] = round(a.min(),2)

    if customer:

        kpi["Unique Customers"] = df[customer].nunique()

    if product:

        kpi["Products Sold"] = df[product].nunique()

    return kpi

# ----------------------------------------------------------
# PRODUCTION KPI
# ----------------------------------------------------------

def production_kpis(df):

    detect = detect_all_columns(df)

    qty = detect["quantity"]

    defect = detect["defect"]

    product = detect["product"]

    kpi = generic_kpis(df)

    if qty:

        q = pd.to_numeric(df[qty],errors="coerce")

        kpi["Total Production"] = round(q.sum(),2)

        kpi["Average Production"] = round(q.mean(),2)

        kpi["Maximum Production"] = round(q.max(),2)

        kpi["Minimum Production"] = round(q.min(),2)

        kpi["Production Std Dev"] = round(q.std(),2)

    if defect:

        d = pd.to_numeric(df[defect],errors="coerce")

        kpi["Total Defective Units"] = round(d.sum(),2)

        if qty:

            total = q.sum()

            if total>0:

                kpi["Defect Percentage"] = round(

                    d.sum()/total*100,

                    2

                )

    if product:

        kpi["Products Manufactured"] = df[product].nunique()

    return kpi

# ----------------------------------------------------------
# INVENTORY KPI
# ----------------------------------------------------------

def inventory_kpis(df):

    detect = detect_all_columns(df)

    opening = detect["opening"]

    closing = detect["closing"]

    consumed = detect["consumed"]

    product = detect["product"]

    kpi = generic_kpis(df)

    if opening:

        o = pd.to_numeric(df[opening],errors="coerce")

        kpi["Opening Inventory"] = round(o.sum(),2)

    if closing:

        c = pd.to_numeric(df[closing],errors="coerce")

        kpi["Closing Inventory"] = round(c.sum(),2)

    if consumed:

        con = pd.to_numeric(df[consumed],errors="coerce")

        kpi["Material Consumed"] = round(con.sum(),2)

    if opening and closing:

        avg = (o.mean()+c.mean())/2

        kpi["Average Inventory"] = round(avg,2)

    if product:

        kpi["Inventory Items"] = df[product].nunique()

    return kpi

# ----------------------------------------------------------
# ATTENDANCE KPI
# ----------------------------------------------------------

def attendance_kpis(df):

    detect = detect_all_columns(df)

    workers = detect["attendance"]

    kpi = generic_kpis(df)

    if workers:

        w = pd.to_numeric(df[workers],errors="coerce")

        kpi["Average Workforce"] = round(w.mean(),2)

        kpi["Maximum Workforce"] = round(w.max(),2)

        kpi["Minimum Workforce"] = round(w.min(),2)

    return kpi

# ----------------------------------------------------------
# MACHINE KPI
# ----------------------------------------------------------

def machine_kpis(df):

    detect = detect_all_columns(df)

    machine = detect["machine"]

    downtime = detect["downtime"]

    kpi = generic_kpis(df)

    if machine:

        kpi["Machines Affected"] = df[machine].nunique()

    if downtime:

        d = pd.to_numeric(df[downtime],errors="coerce")

        kpi["Total Downtime"] = round(d.sum(),2)

        kpi["Average Downtime"] = round(d.mean(),2)

        kpi["Maximum Downtime"] = round(d.max(),2)

    return kpi

# ----------------------------------------------------------
# CAPACITY KPI
# ----------------------------------------------------------

def capacity_kpis(df):

    detect = detect_all_columns(df)

    cap = detect["capacity"]

    kpi = generic_kpis(df)

    if cap:

        c = pd.to_numeric(df[cap],errors="coerce")

        kpi["Installed Capacity"] = round(c.sum(),2)

        kpi["Average Capacity"] = round(c.mean(),2)

        kpi["Maximum Capacity"] = round(c.max(),2)

    return kpi

# ----------------------------------------------------------
# AUTO DETECT DATASET TYPE
# ----------------------------------------------------------

for name,df in datasets.items():

    lower = name.lower()

    if "purchase" in lower:

        all_kpis[name] = purchase_kpis(df)

    elif "sales" in lower:

        all_kpis[name] = sales_kpis(df)

    elif "production" in lower:

        all_kpis[name] = production_kpis(df)

    elif "inventory" in lower:

        all_kpis[name] = inventory_kpis(df)

    elif "attendance" in lower:

        all_kpis[name] = attendance_kpis(df)

    elif "breakdown" in lower:

        all_kpis[name] = machine_kpis(df)

    elif "capacity" in lower:

        all_kpis[name] = capacity_kpis(df)

    else:

        all_kpis[name] = generic_kpis(df)

print("\n")
print("="*80)
print("KPI SUMMARY")
print("="*80)

for dataset,kpi in all_kpis.items():

    print("\n",dataset)

    print("-"*60)

    for key,val in kpi.items():

        print(f"{key:35} : {val}")

