"""
========================================================================================
FOOD DELIVERY PERFORMANCE EXPLORATORY DATA ANALYSIS (EDA)
Course / Assessment: Advanced Excel for Data Analytics (M3-A1)
Task: Task 4 — Delivery Performance EDA (Python + pandas)
Student Name: Mahek Sarkhedi
========================================================================================
"""

import pandas as pd
import numpy as np

def run_eda():
    # ----------------------------------------------------------------------------------
    # Step 1: Load Dataset from CSV Export of Excel Table
    # ----------------------------------------------------------------------------------
    csv_file = "orders_data.csv"
    print("=" * 80)
    print("TASK 4: DELIVERY PERFORMANCE EDA — PYTHON (PANDAS)")
    print("=" * 80)
    print(f"Loading dataset from: {csv_file} ...\n")
    
    df = pd.read_csv(csv_file)
    print(f"Dataset successfully loaded. Total Records: {len(df)}, Total Features: {len(df.columns)}")
    print("-" * 80)

    # ----------------------------------------------------------------------------------
    # Step 2: Replicate Descriptive Statistics Using .describe() and Manual IQR
    # ----------------------------------------------------------------------------------
    delivery_series = df["DeliveryTime"]
    desc = delivery_series.describe()

    # Manual IQR and Boundary Calculations
    q1 = float(delivery_series.quantile(0.25))
    q3 = float(delivery_series.quantile(0.75))
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    mode_val = float(delivery_series.mode()[0])
    variance_val = float(delivery_series.var(ddof=1)) # Sample variance matching Excel VAR.S

    # Identify outliers using IQR rule
    outliers = df[(df["DeliveryTime"] < lower_bound) | (df["DeliveryTime"] > upper_bound)]

    print("\n[PART 1] DESCRIPTIVE STATISTICS SUMMARY: DELIVERY TIME (MINUTES)")
    print("=" * 80)
    stats_table = pd.DataFrame([
        {"Metric": "Count", "Formula / Source": "len(df)", "Value": f"{int(desc['count'])}", "Notes": "Total order sample size"},
        {"Metric": "Mean", "Formula / Source": "df['DeliveryTime'].mean()", "Value": f"{desc['mean']:.2f} mins", "Notes": "Arithmetic average wait time"},
        {"Metric": "Median", "Formula / Source": "df['DeliveryTime'].median()", "Value": f"{desc['50%']:.2f} mins", "Notes": "50th percentile (typical experience)"},
        {"Metric": "Mode", "Formula / Source": "df['DeliveryTime'].mode()[0]", "Value": f"{mode_val:.2f} mins", "Notes": "Most frequently observed wait time"},
        {"Metric": "Standard Deviation", "Formula / Source": "df['DeliveryTime'].std()", "Value": f"{desc['std']:.2f} mins", "Notes": "Sample standard deviation (spread)"},
        {"Metric": "Sample Variance", "Formula / Source": "df['DeliveryTime'].var()", "Value": f"{variance_val:.2f} mins^2", "Notes": "Variance around the mean"},
        {"Metric": "Minimum", "Formula / Source": "df['DeliveryTime'].min()", "Value": f"{desc['min']:.2f} mins", "Notes": "Fastest delivery recorded"},
        {"Metric": "Maximum", "Formula / Source": "df['DeliveryTime'].max()", "Value": f"{desc['max']:.2f} mins", "Notes": "Slowest delivery recorded"},
        {"Metric": "25th Percentile (Q1)", "Formula / Source": "quantile(0.25)", "Value": f"{q1:.2f} mins", "Notes": "25% of deliveries completed within"},
        {"Metric": "75th Percentile (Q3)", "Formula / Source": "quantile(0.75)", "Value": f"{q3:.2f} mins", "Notes": "75% of deliveries completed within"},
        {"Metric": "Interquartile Range (IQR)", "Formula / Source": "Q3 - Q1", "Value": f"{iqr:.2f} mins", "Notes": "Spread of the middle 50% orders"},
        {"Metric": "Lower Outlier Bound", "Formula / Source": "Q1 - 1.5 * IQR", "Value": f"{lower_bound:.2f} mins", "Notes": "Threshold for abnormally fast times"},
        {"Metric": "Upper Outlier Bound", "Formula / Source": "Q3 + 1.5 * IQR", "Value": f"{upper_bound:.2f} mins", "Notes": "Threshold for severe delivery delays"},
        {"Metric": "Flagged Outliers Count", "Formula / Source": "IQR Rule", "Value": f"{len(outliers)} orders", "Notes": "Deliveries outside bounds (Outlier Flag='Yes')"}
    ])
    
    print(stats_table.to_string(index=False))
    print("-" * 80)
    
    print("\nDetailed Outlier Records (DeliveryTime > Upper Bound):")
    print(outliers[["OrderID", "CustomerName", "Cuisine", "DeliveryTime", "Rating", "Revenue", "Status"]].to_string(index=False))
    print("-" * 80)

    # ----------------------------------------------------------------------------------
    # Step 3: Correlation Matrix Calculation and Business Implications
    # ----------------------------------------------------------------------------------
    corr_vars = ["DeliveryTime", "Revenue", "Rating"]
    corr_matrix = df[corr_vars].corr()

    print("\n[PART 2] CORRELATION MATRIX (DeliveryTime vs. Revenue vs. Rating)")
    print("=" * 80)
    print(corr_matrix.round(4).to_string())
    print("=" * 80)

    # ----------------------------------------------------------------------------------
    # Step 4: Business Insights & Strategic Implications
    # ----------------------------------------------------------------------------------
    # Inline Comment Line 1: DeliveryTime vs Rating (-0.8275) shows a severe inverse relationship: longer wait times are the primary driver of low customer ratings, proving operational delivery speed directly governs customer retention.
    # Inline Comment Line 2: Revenue vs DeliveryTime (+0.2618) shows a moderate positive correlation: higher-value orders have larger basket sizes requiring longer kitchen food preparation, signaling the need for dedicated staging for large orders.
    # Inline Comment Line 3: Revenue vs Rating (+0.1163) reveals a weak positive correlation: customers spending more money do not automatically give higher ratings unless fast delivery logistics are consistently maintained.

    print("\nBUSINESS IMPLICATIONS DERIVED FROM CORRELATION ANALYSIS:")
    print("1. DeliveryTime vs. Rating (-0.83): Strong Negative Correlation")
    print("   -> Delivery delay is the single biggest determinant of customer dissatisfaction.")
    print("   -> Operations must prioritize routing algorithms, dispatch SLA, and driver allocation.")
    print("2. Revenue vs. DeliveryTime (+0.26): Moderate Positive Correlation")
    print("   -> Higher revenue orders represent larger food portions requiring longer kitchen preparation times.")
    print("   -> The platform should implement dynamic prep-time buffer estimates for large group orders.")
    print("3. Revenue vs. Rating (+0.12): Weak Positive Correlation")
    print("   -> High ticket size alone does not buy customer loyalty; rating is dominated by delivery punctuality.")
    print("=" * 80)

if __name__ == "__main__":
    run_eda()
