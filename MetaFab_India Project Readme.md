# 🏭 MetaFab India — Production Planning Analytics

<div align="center">

### 📊 Turning messy factory data into smarter production decisions

**BDM Capstone Project | IIT Madras**

🏗️ Manufacturing & Operations  
📦 Inventory & Procurement  
📈 Demand Analytics  
⚙️ Production Planning  
🐍 Python + 📗 Excel  

</div>

---

## 🚀 What is this project?

MetaFab India is an MSME-based B2B manufacturer of **gas stove components** in Greater Noida, India.

The business maintains a large part of its operational information through manual records. That creates a classic operations problem:

> **How do you decide what to buy, what to produce, how much to keep in stock, and when to produce — without creating unnecessary inventory or delaying customer orders? 🤯**

This project turns those fragmented operational records into a **data-driven production-planning framework**.

---

## 🎯 Business Problem

MetaFab operates under a tricky trade-off:

```text
Produce only after receiving an order
        ↓
✅ Lower inventory risk
❌ Higher fulfilment pressure

Produce before receiving an order
        ↓
✅ Faster fulfilment
❌ Higher inventory / working-capital risk
```

So the real question becomes:

### 🧠 What should MetaFab produce, how much should it prepare in advance, and when should it remain make-to-order?

---

## 💡 Project Objectives

### 1️⃣ Procurement Alignment
Evaluate whether raw-material purchases and inventory levels are aligned with actual production requirements.

### 2️⃣ Production Efficiency
Assess production output against demand, capacity, labour availability and machine-related constraints.

### 3️⃣ Demand-Based Planning
Use historical demand patterns to generate short-term production-planning signals.

---

## 📂 Data Used

The project uses **primary business data** digitised from MetaFab's operational records.

### 8 datasets 📚

| Dataset | What it tells us |
|---|---|
| 🧾 Purchase Data | Raw-material procurement |
| 🛒 Sales Invoices | Customer demand & revenue |
| 🏭 Production Data | Output, material use & defects |
| 📏 Production Capacity | Practical production limits |
| 👷 Attendance Log | Workforce availability |
| 🔧 Machine Breakdown Log | Downtime & failure patterns |
| 📦 Raw-Material Inventory | Material inflow, consumption & stock |
| 📦 Finished-Goods Inventory | Production, sales & stock movement |

📌 **2,529 operational records**  
📅 **Approx. January–June 2026**  
🗂️ **8 datasets**

---

# 🔬 Analysis Pipeline

```text
🏢 Business Problem
        ↓
📥 Data Collection
        ↓
🧹 Data Cleaning & Validation
        ↓
📊 Descriptive Statistics
        ↓
🔄 Material Flow Analysis
        ↓
💰 Procurement & Inventory Analysis
        ↓
📦 Demand & Production Analysis
        ↓
⚙️ Capacity & Operational Analysis
        ↓
🔗 Correlation / Regression Screening
        ↓
🔮 Short-Term Demand Signal
        ↓
🧠 Business Interpretation
        ↓
🚀 Recommendations
```

---

# 🧰 Tech Stack

### 💻 Analytics
- 🐍 Python
- 🐼 Pandas
- 🔢 NumPy
- 📊 Statistical analysis

### 📗 Business Analysis
- Microsoft Excel
- Descriptive statistics
- KPI analysis
- Material Flow Analysis

### 📈 Visual Analytics
- Matplotlib
- Exploratory data visualisation

---

# 📊 Key Analyses

## 🔄 Material Flow Analysis

Tracks how material moves through the system:

$$
Opening\ Stock + Inflow - Outflow = Closing\ Stock
$$

This helps identify where materials are:

✅ being consumed efficiently  
⚠️ accumulating  
🚨 becoming potential inventory risks

---

## 📦 Procurement Analytics

We analysed:

- Purchase quantity
- Purchase frequency
- Procurement cost
- Material-wise purchasing behaviour
- Variability
- Inventory coverage

### One important finding 👀

Purchase quantity showed a **~73.15% coefficient of variation**, while procurement cost showed **~77.57%**.

Translation:

> Procurement is **far from uniform**. Average purchase quantity alone isn't enough for planning.

---

## 🏭 Production Analytics

We analysed:

- Good units produced
- Defective units
- Material consumption
- Product-level production
- Production variability
- Capacity utilisation

📌 Total good production: **185,173 units**

📌 Overall defect rate: **~4.63%**

---

## ⚙️ Capacity Analysis

Capacity utilisation on recorded production days is approximately:

### **57–59%**

This does **not** automatically mean the plant is under-utilised.

Capacity also depends on:

- 📦 product mix
- 🧾 customer orders
- 🧱 material availability
- 🔧 machine availability
- 👷 workforce availability
- 🗓️ production scheduling

So the smarter question is:

> **How should existing capacity be allocated?**

—not simply—

> "Should MetaFab buy more machines?"

---

## 🔧 Machine Reliability

Recorded machine downtime:

### **73.1 hours**

Two operating areas account for roughly **80% of recorded downtime**:

🥇 Casting Line & Fettling  
🥈 Brass CNC & Turning Cell

This gives management a clear place to start with preventive-maintenance efforts.

---

## 📈 Demand Analytics

The sales dataset contains multiple products, while production/capacity records cover the three products supported by manufacturing data.

For those common products, we analysed:

- 📊 demand volume
- 📆 monthly trends
- 📅 weekly variability
- 💰 revenue contribution
- 🔥 product concentration

### Gas Valve Assembly stands out

It is the largest manufactured-product demand contributor and also has the highest weekly demand variability at approximately **56.5% CV**.

That makes it an important candidate for deeper planning analysis.

---

# 🔮 Short-Term Demand Planning

A **3-month weighted moving average** was used as a transparent short-term planning signal.

Weights:

```text
April   → 1️⃣
May     → 2️⃣
June    → 3️⃣
```

Why WMA?

✅ Simple  
✅ Transparent  
✅ Easy to reproduce in Excel  
✅ Gives more importance to recent demand  
✅ Works with a relatively short historical series

⚠️ These are **planning signals**, not guaranteed forecasts or automatic production targets.

---

# 🧠 Big Insights

### 🔥 Insight #1 — Procurement is highly variable
Large swings in purchase quantity and cost mean procurement decisions should be evaluated against actual inventory requirements.

### 📦 Insight #2 — Inventory is not equally healthy across materials
Some materials accumulate heavily while others move toward lower coverage.

Example:

**Cast Iron Scrap**

- Opening stock: **7,200 kg**
- Closing stock: **23,593 kg**
- Approx. coverage: **114.7 days**

🚨 This deserves a procurement review.

### 🏭 Insight #3 — More capacity is not automatically the answer
The business has some capacity headroom on recorded production days.

The bigger issue is **allocation + timing + coordination**.

### 🔧 Insight #4 — Downtime is concentrated
A relatively small number of operating areas account for most recorded downtime.

🎯 Maintenance can therefore be targeted instead of being spread uniformly.

### 🧩 Insight #5 — Production planning needs multiple signals
No single variable explains the business problem.

A better planning decision combines:

```text
📈 Demand
+
📦 Inventory
+
🧱 Material Availability
+
🏭 Capacity
+
🔧 Machine Constraints
+
👷 Workforce
=
🧠 Production Decision
```

---

# 🚀 Recommended Production-Planning Framework

```text
1️⃣ Demand Signal
        ↓
2️⃣ Inventory Position
        ↓
3️⃣ Capacity Check
        ↓
4️⃣ Machine + Workforce Check
        ↓
5️⃣ Make-to-Stock / Make-to-Order Decision
        ↓
6️⃣ Execute & Monitor
        ↓
7️⃣ Monthly Recalibration
```

### ⚡ Decision principle

> **Don't pre-produce just because capacity is available.**

Pre-production should be considered when:

✅ demand is recurring  
✅ fulfilment pressure is meaningful  
✅ required materials are available  
✅ inventory remains within a controlled buffer

Otherwise:

👉 stay **make-to-order** while improving material readiness and production availability.

---

# 📌 Recommendations

### 🧱 1. Material-Specific Procurement Review
Review every raw material using:

**consumption + stock coverage + recent purchases + supplier lead time**

---

### 📦 2. Separate Make-to-Stock vs Make-to-Order

Not every product deserves the same inventory strategy.

Use product-level:

- demand frequency
- demand variability
- fulfilment requirement
- capacity availability

---

### 🔮 3. Use a Short-Term Demand Signal

Recalculate the weighted demand signal monthly as fresh customer-order information becomes available.

---

### 🔧 4. Prioritise High-Downtime Areas

Focus preventive maintenance on the operating areas contributing most to downtime.

---

### 🏭 5. Use Existing Capacity Before Expanding

Improve product mix and scheduling before committing capital to additional capacity.

---

### 🧾 6. Capture Better Order-Level Data

Future records should include:

- Order received date
- Promised dispatch date
- Actual dispatch date
- Order quantity
- Product

This makes fulfilment performance measurable. 🎯

---

### 🧩 7. Build a Bill of Materials Mapping

Map:

**Product → Raw Material → Standard Quantity**

This unlocks proper product-level procurement and material planning.

---

# ⚠️ Important Data Limitations

No pretending the data is perfect. 😌

- 📅 Only ~6 months of history → long-term seasonality cannot be established reliably.
- 🔧 Only 18 machine-breakdown events → downtime relationships are directional.
- 🔄 Transaction and inventory ledgers have different scopes and do not reconcile one-to-one.
- 🏷️ Sales contain more products than the manufacturing datasets.
- 🧾 Order-received / promised-dispatch / actual-dispatch timestamps are unavailable.
- 🧩 A verified product-to-material BOM was not available.
- 🔮 Short-term demand signals should be recalculated as more observations become available.

---

# 📁 Repository Structure

```text
MetaFab-BDM/
│
├── 📂 data/
│   └── MetaFab_Mastersheet.xlsx
│
├── 📂 notebooks/
│   ├── data_cleaning.ipynb
│   ├── exploratory_analysis.ipynb
│   └── production_planning_analysis.ipynb
│
├── 📂 src/
│   └── metafab_analysis.py
│
├── 📂 outputs/
│   ├── analysis_results/
│   └── figures/
│
├── 📂 report/
│   └── BDM_Final_Report.pdf
│
└── 📄 README.md
```

---

# 🎓 Academic Context

**Course:** BDM Capstone Project  
**Programme:** IIT Madras — Online BS Degree Program  
**Project Type:** Primary Data Business Analytics  
**Domain:** Manufacturing & Production Planning

---

# 🌟 Why this project matters

This project is less about making pretty charts and more about answering a real business question:

> **How can operational data help a manufacturing business make better production decisions?**

The outcome is a practical framework connecting:

**📈 Demand → 📦 Inventory → 🧱 Materials → 🏭 Capacity → 🔧 Constraints → 🚀 Production Decisions**

That's the whole game. 🎯

---

<div align="center">

### 🏭 MetaFab India × 📊 Data Analytics × 🧠 Better Decisions

**From handwritten registers → structured data → actionable intelligence.**

</div>
