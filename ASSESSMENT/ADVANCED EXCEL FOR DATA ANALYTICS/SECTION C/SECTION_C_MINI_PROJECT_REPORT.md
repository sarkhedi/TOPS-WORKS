# Mini Project: Food Delivery Operations Dashboard — Excel Edition
**Module:** Advanced Excel for Data Analytics (`M3-A1`)  
**Section:** Section C (Mini Project)  
**Candidate Name:** Mahek Sarkhedi  
**Files in `SECTION C`:**
1. Excel Workbook: [`MahekSarkhedi_Food_Delivery_Operations_Dashboard.xlsx`](file:///e:/TOPS-WORKS/ASSESMENT/ADVANCED%20EXCEL%20FOR%20DATA%20ANALYTICS/SECTION%20C/MahekSarkhedi_Food_Delivery_Operations_Dashboard.xlsx)
2. Raw Orders Dataset: [`orders_miniproject.csv`](file:///e:/TOPS-WORKS/ASSESMENT/ADVANCED%20EXCEL%20FOR%20DATA%20ANALYTICS/SECTION%20C/orders_miniproject.csv)
3. Raw Restaurants Reference Data: [`restaurants_miniproject.csv`](file:///e:/TOPS-WORKS/ASSESMENT/ADVANCED%20EXCEL%20FOR%20DATA%20ANALYTICS/SECTION%20C/restaurants_miniproject.csv)
4. Comprehensive Project Report: [`SECTION_C_MINI_PROJECT_REPORT.md`](file:///e:/TOPS-WORKS/ASSESMENT/ADVANCED%20EXCEL%20FOR%20DATA%20ANALYTICS/SECTION%20C/SECTION_C_MINI_PROJECT_REPORT.md)

---

## 1. Project Overview & Architecture
This project delivers a multi-layer operations dashboard for a food delivery platform. An operations manager can analyze high-level KPIs, filter regional performance, evaluate cuisine contribution, and audit delivery latency without touching raw transactional data.

### Workbook Structure:
1. **`Dashboard`**: Executive reporting view featuring 3 dynamic KPI cards, two connected Pivot Tables, a shared Zone Slicer, and an interactive date Timeline Slicer.
2. **`Zone Stats`**: Granular statistical summary evaluating Mean, Median, and Sample Standard Deviation for both delivery duration and order revenue across all 5 zones, with conditional median benchmark auditing.
3. **`Orders`**: 120-row transactional master table (`tblOrders`) enriched dynamically via dual `XLOOKUP` functions and highlighted using a Top 10% Revenue conditional formatting rule.
4. **`Restaurants`**: 16-row reference dimension table (`tblRestaurants`) detailing restaurant partners, operational zones, restaurant categories, and customer ratings.

---

## 2. Component Breakdown & Formula Implementation

### Component 1: Master Data Enrichment (`Orders` & `Restaurants`)
* **Orders Dataset Size:** 120 rows spanning Q1 2024 (January 1 to March 31, 2024), 5 delivery zones (`North`, `South`, `East`, `West`, `Central`), and 4 cuisine categories (`North Indian`, `Italian`, `Chinese`, `Biryani`).
* **Table Definition:** `tblOrders`.
* **Dynamic Lookups (`XLOOKUP` with Error Handling):**
  * **Restaurant Name (Column C):**
    ```excel
    =XLOOKUP(B2, Restaurants!$A$2:$A$17, Restaurants!$B$2:$B$17, "Unknown")
    ```
  * **Restaurant Category (Column D):**
    ```excel
    =XLOOKUP(B2, Restaurants!$A$2:$A$17, Restaurants!$D$2:$D$17, "Unknown")
    ```
  * *Audit Proof:* Rows with unmapped restaurant ID `R999` (e.g. `ORD2015` and `ORD2068`) display `"Unknown"` cleanly, suppressing `#N/A` errors that would corrupt downstream analytics.
* **Top 10% Conditional Formatting:**
  * Applied to the `Revenue` column (`tblOrders[Revenue]`).
  * High-value orders falling within the upper 10th percentile are automatically highlighted with soft green fill (`#C6EFCE`) and bold dark green text (`#006100`).

---

### Component 2: Statistical Summary Sheet (`Zone Stats`)
This sheet calculates parametric and non-parametric central tendency and dispersion metrics by zone:
* **Benchmark Overall Median DeliveryTime (Cell `C2`):**
  ```excel
  =MEDIAN(tblOrders[DeliveryTime])
  ```
  *(Result: 33.00 minutes)*

#### Zone Summary Matrix:
| Zone | DeliveryTime Mean | DeliveryTime Median | DeliveryTime StdDev | Revenue Mean | Revenue Median | Revenue StdDev | Status vs. Overall Median |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **North** | 28.11 mins | 28.00 mins | 7.64 mins | ₹808.52 | ₹790.00 | ₹368.90 | Normal (<= Median) |
| **South** | 32.45 mins | 32.00 mins | 8.71 mins | ₹846.36 | ₹850.00 | ₹372.41 | Normal (<= Median) |
| **East** | 28.96 mins | 28.00 mins | 8.37 mins | ₹910.00 | ₹1,060.00 | ₹396.42 | Normal (<= Median) |
| **West** | 38.56 mins | 38.00 mins | 6.80 mins | ₹984.40 | ₹1,110.00 | ₹383.99 | **FLAGGED (Above Median)** |
| **Central** | 36.59 mins | 36.50 mins | 9.52 mins | ₹810.00 | ₹710.00 | ₹377.16 | **FLAGGED (Above Median)** |

#### Applied Formulas in Matrix:
1. **DeliveryTime Mean:** `=AVERAGEIF(tblOrders[Zone], A5, tblOrders[DeliveryTime])`
2. **DeliveryTime Median:** Array formula `{=MEDIAN(IF(tblOrders[Zone]=A5, tblOrders[DeliveryTime]))}`
3. **DeliveryTime StdDev:** Array formula `{=STDEV.S(IF(tblOrders[Zone]=A5, tblOrders[DeliveryTime]))}`
4. **Revenue Mean:** `=AVERAGEIF(tblOrders[Zone], A5, tblOrders[Revenue])`
5. **Revenue Median:** Array formula `{=MEDIAN(IF(tblOrders[Zone]=A5, tblOrders[Revenue]))}`
6. **Revenue StdDev:** Array formula `{=STDEV.S(IF(tblOrders[Zone]=A5, tblOrders[Revenue]))}`
7. **Conditional Benchmark Flag:**
   ```excel
   =IF(B5>$C$2, "FLAGGED (Above Median)", "Normal (<= Median)")
   ```
   *(Enhanced with soft red conditional formatting highlighting West and Central as delivery bottleneck zones).*

---

### Component 3: Executive KPI Summary Cards (`Dashboard`)
Positioned above the pivot tables (Rows 3–4) for immediate executive visibility:
1. **Total Revenue (Cell `B4`):**
   ```excel
   =SUM(tblOrders[Revenue])
   ```
   *Value:* **₹1,04,720** (Formatted as Indian Rupee currency).
2. **Average Customer Rating (Cell `E4`):**
   ```excel
   =AVERAGE(tblOrders[Rating])
   ```
   *Value:* **4.01** (Formatted to 2 decimal places).
3. **On-Time Delivery % (Cell `H4`):**
   ```excel
   =COUNTIFS(tblOrders[Status], "Delivered", tblOrders[DeliveryTime], "<=40") / COUNTA(tblOrders[OrderID])
   ```
   *Value:* **65.8%** (Measures successfully completed deliveries completed within the 40-minute SLA).

---

### Component 4: Interactive Pivot Tables, Shared Slicer & Timeline (`Dashboard`)
1. **Pivot Table 1 (`ptRevenueCuisineZone` at `A8`):**
   * **Rows:** `Cuisine` (North Indian, Italian, Chinese, Biryani).
   * **Columns:** `Zone` (North, South, East, West, Central).
   * **Values:** `Sum of Revenue` formatted as Currency (`₹#,##0`).
   * **Totals:** Row and Column Grand Totals enabled.
2. **Pivot Table 2 (`ptMonthlyOrderCount` at `A19`):**
   * **Rows:** `OrderDate` grouped by `Months` (January, February, March).
   * **Values:** `Count of OrderID`.
3. **Shared Zone Slicer (`Slicer_Zone_UI`):**
   * Placed at coordinates Top: 120, Left: 520.
   * **Cross-Pivot Connectivity:** Wired via VBA/COM cache (`SlicerCaches("Slicer_Zone").PivotTables.AddPivotTable(pt2)`) so clicking any zone instantly filters **both** the Revenue by Cuisine breakdown and the Monthly Order Trends table simultaneously.
4. **Interactive Timeline Slicer (`Timeline_Date_UI`):**
   * Placed alongside the Zone Slicer at Top: 120, Left: 700.
   * Enables one-click chronological sliding across days, months, and quarters.

---

## 3. Operational Findings for Management
* **Regional Disparity:** `West` (38.56 min) and `Central` (36.59 min) significantly breach the overall median latency (33.00 min), indicating traffic congestion and kitchen dispatch bottlenecks.
* **Logistics Efficiency:** `North` achieves the lowest delivery time (28.11 min) with high customer satisfaction, providing an operational benchmark for other zones.
* **On-Time Performance:** The current 65.8% on-time delivery rate demonstrates that approximately 1 in 3 deliveries experiences latency; routing optimizations in West and Central are required to achieve the platform's target 80% SLA.
