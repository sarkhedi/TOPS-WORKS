# Section D: AI-Assisted Development, Testing & Debugging Report
**Module:** Advanced Excel for Data Analytics (`M3-A1`)  
**Section:** Section D — Build with AI & Test/Debug Without AI  
**Candidate Name:** Mahek Sarkhedi  
**Working Directory:** `SECTION D`

---

## 1. The Exact Prompt(s) Given to the AI Tool (Step 1)

```text
"Act as a Python data analyst. Write a clean Python script using pandas that:
1. Reads a food delivery orders CSV file named 'food_orders_test_data.csv' containing columns: OrderID, CustomerName, Cuisine, DeliveryTime, Revenue, Status.
2. Produces a summary table showing Total Revenue, Average DeliveryTime, and Order Count grouped by Cuisine.
3. Adds a new column named PerformanceFlag that labels any row with DeliveryTime > 60 as 'Delayed' and all others as 'On Time'.
4. Saves the cleaned and enriched output as a new file named food_delivery_summary.xlsx using pandas ExcelWriter with two sheets: 'Enriched_Orders' and 'Cuisine_Summary'.
5. Must run without raising an error on a dataset where some Revenue cells are blank (NaN) and at least one DeliveryTime value is negative (a data entry error)."
```

---

## 2. Code Comparison: AI's Original Script vs. Corrected Script (Step 2)

### A. The AI's Original Script (`ai_original_script.py`)
```python
import pandas as pd
import numpy as np

# Step 1: Read the CSV file
df = pd.read_csv("food_orders_test_data.csv")

# Step 2: Add PerformanceFlag column (naive binary condition)
# BUG: Negative delivery time (e.g. -5) evaluates as <= 60, incorrectly marked as 'On Time'!
df['PerformanceFlag'] = np.where(df['DeliveryTime'] > 60, 'Delayed', 'On Time')

# Step 3: Produce summary table grouped by Cuisine
# BUG 1: The -5 delivery time is included in the mean, severely skewing the average!
# BUG 2: Rows with NaN Cuisine are silently dropped by groupby, losing revenue and order count!
summary_df = df.groupby('Cuisine').agg(
    Total_Revenue=('Revenue', 'sum'),
    Average_DeliveryTime=('DeliveryTime', 'mean'),
    Order_Count=('OrderID', 'count')
).reset_index()

# Step 4: Save to Excel using pandas ExcelWriter
with pd.ExcelWriter("food_delivery_summary_ai.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Enriched_Orders", index=False)
    summary_df.to_excel(writer, sheet_name="Cuisine_Summary", index=False)
```

---

### B. The Corrected Production Script (`corrected_script.py`)
```python
import pandas as pd
import numpy as np

# Step 1: Read raw CSV with type coercion
df = pd.read_csv("food_orders_test_data.csv")

# FIX 1: Prevent silent dropping of records with missing Cuisine
df['Cuisine'] = df['Cuisine'].fillna('Unspecified / Other')

# FIX 2: Validate Revenue column and coerce data types
df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')

# FIX 3: Multi-condition classification for PerformanceFlag (prevent negative times marked as 'On Time')
df['DeliveryTime'] = pd.to_numeric(df['DeliveryTime'], errors='coerce')
conditions = [
    df['DeliveryTime'].isna(),
    df['DeliveryTime'] < 0,
    df['DeliveryTime'] > 60,
    (df['DeliveryTime'] >= 0) & (df['DeliveryTime'] <= 60)
]
choices = [
    'Missing Time',
    'Data Error (Negative Time)',
    'Delayed',
    'On Time'
]
df['PerformanceFlag'] = np.select(conditions, choices, default='Unclassified')

# FIX 4: Exclude corrupted negative times from Average DeliveryTime calculations
df['Clean_DeliveryTime'] = np.where(df['DeliveryTime'] >= 0, df['DeliveryTime'], np.nan)

summary_df = df.groupby('Cuisine').agg(
    Total_Revenue=('Revenue', 'sum'),
    Average_DeliveryTime=('Clean_DeliveryTime', 'mean'),
    Order_Count=('OrderID', 'count'),
    Valid_Delivery_Orders=('Clean_DeliveryTime', 'count'),
    Data_Error_Count=('DeliveryTime', lambda x: (x < 0).sum()),
    Blank_Revenue_Count=('Revenue', lambda x: x.isna().sum())
).reset_index()

summary_df['Total_Revenue'] = summary_df['Total_Revenue'].round(2)
summary_df['Average_DeliveryTime'] = summary_df['Average_DeliveryTime'].round(2)

# Step 5: Save cleaned output with formatting
df_export = df.drop(columns=['Clean_DeliveryTime'])
with pd.ExcelWriter("food_delivery_summary.xlsx", engine="openpyxl") as writer:
    df_export.to_excel(writer, sheet_name="Enriched_Orders", index=False)
    summary_df.to_excel(writer, sheet_name="Cuisine_Summary", index=False)
```

---

## 3. Written Note: Bug Analysis & Explanation

> **Written Note (Required 3–4 Lines):**  
> **1. What was changed:** We replaced the naive binary `np.where` with a multi-condition `np.select` rule that labels negative and missing delivery durations as `'Data Error'`, excluded negative values from the `Average_DeliveryTime` calculation, and filled missing `Cuisine` values with `'Unspecified'` before grouping.  
> **2. Specific input that exposed the bug:** Record `ORD3005` with `DeliveryTime = -5` and record `ORD3021` with `Cuisine = NaN`.  
> **3. Why the AI failed:** The AI's condition `DeliveryTime > 60` naively evaluated `-5 > 60` as `False`, incorrectly categorizing an impossible negative time as `'On Time'` and pulling North Indian average delivery time down from 45.60 to 37.17 minutes, while pandas' default `groupby('Cuisine')` silently dropped `ORD3021`, losing ₹610 in reported platform revenue.

---

## 4. Test Results Comparison Table

| Metric / Scenario | AI Original Script | Corrected Script | Operational Impact / Explanation |
| :--- | :---: | :---: | :--- |
| **`ORD3005` (`DeliveryTime = -5`) Flag** | `'On Time'` | `'Data Error (Negative Time)'` | AI falsely praised a severe data entry glitch as punctual delivery. |
| **North Indian Average DeliveryTime** | **37.17 mins** | **45.60 mins** | AI understated true delivery latency by **8.43 minutes (18.5% error)** due to negative number inclusion. |
| **Missing Cuisine Order (`ORD3021`)** | **Silently Dropped** | **Preserved (`Unspecified`)** | AI lost track of 1 order and omitted ₹610 in platform revenue. |
| **Total Orders in Summary** | 24 orders | 25 orders | Corrected version accounts for 100% of customer orders. |
| **Data Quality Visibility** | None (Hidden) | Audit columns added | Operations now tracks blank revenues and negative time logs. |
