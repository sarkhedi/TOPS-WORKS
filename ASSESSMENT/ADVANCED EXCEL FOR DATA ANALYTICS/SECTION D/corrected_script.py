"""
========================================================================================
SECTION D (STEP 2): HUMAN-TESTED & CORRECTED PRODUCTION SCRIPT
Author: Mahek (Data Analyst)
Module: Advanced Excel for Data Analytics (M3-A1)
Task: Section D — AI Debugging, Edge Case Testing & Code Correction
Target Output: food_delivery_summary.xlsx
========================================================================================
"""

import os
import pandas as pd
import numpy as np

def run_corrected_pipeline():
    print("=" * 80)
    print("SECTION D: CORRECTED DATA CLEANING & SUMMARY PIPELINE")
    print("=" * 80)
    
    input_csv = "food_orders_test_data.csv"
    output_excel = "food_delivery_summary.xlsx"
    
    # ----------------------------------------------------------------------------------
    # 1. Read Raw CSV with Data Integrity Checks
    # ----------------------------------------------------------------------------------
    print(f"Loading raw dataset from '{input_csv}' ...")
    df = pd.read_csv(input_csv)
    raw_count = len(df)
    print(f"Loaded {raw_count} raw order records.\n")
    
    # ----------------------------------------------------------------------------------
    # 2. Fix Bug #1: Handle Missing/Blank Cuisines
    #    (AI bug: Naive groupby silently drops NaN cuisines, losing orders and revenue)
    # ----------------------------------------------------------------------------------
    df['Cuisine'] = df['Cuisine'].fillna('Unspecified / Other')
    
    # ----------------------------------------------------------------------------------
    # 3. Fix Bug #2: Coerce & Validate Revenue
    #    (Ensure blank/NaN cells are treated safely without crashing or hiding data gaps)
    # ----------------------------------------------------------------------------------
    df['Revenue'] = pd.to_numeric(df['Revenue'], errors='coerce')
    missing_rev_count = df['Revenue'].isna().sum()
    print(f"[Data Quality Audit] Missing/Blank Revenue cells identified: {missing_rev_count}")
    
    # ----------------------------------------------------------------------------------
    # 4. Fix Bug #3: Negative Delivery Times & Comprehensive PerformanceFlag
    #    (AI bug: -5 was categorized as 'On Time' because -5 > 60 evaluated to False)
    # ----------------------------------------------------------------------------------
    df['DeliveryTime'] = pd.to_numeric(df['DeliveryTime'], errors='coerce')
    negative_time_count = (df['DeliveryTime'] < 0).sum()
    print(f"[Data Quality Audit] Negative DeliveryTime errors identified: {negative_time_count}")
    
    # Robust multi-condition classification
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
    
    # ----------------------------------------------------------------------------------
    # 5. Fix Bug #4: Clean Metric Aggregation
    #    (Exclude negative delivery times from Average DeliveryTime so averages reflect reality)
    # ----------------------------------------------------------------------------------
    # Create clean delivery time series for aggregation (treating <0 as NaN so mean ignores it)
    df['Clean_DeliveryTime'] = np.where(df['DeliveryTime'] >= 0, df['DeliveryTime'], np.nan)
    
    summary_df = df.groupby('Cuisine').agg(
        Total_Revenue=('Revenue', 'sum'),
        Average_DeliveryTime=('Clean_DeliveryTime', 'mean'),
        Order_Count=('OrderID', 'count'),
        Valid_Delivery_Orders=('Clean_DeliveryTime', 'count'),
        Data_Error_Count=('DeliveryTime', lambda x: (x < 0).sum()),
        Blank_Revenue_Count=('Revenue', lambda x: x.isna().sum())
    ).reset_index()
    
    # Round metrics for presentation
    summary_df['Total_Revenue'] = summary_df['Total_Revenue'].round(2)
    summary_df['Average_DeliveryTime'] = summary_df['Average_DeliveryTime'].round(2)
    
    # Drop intermediate helper column from export table
    df_export = df.drop(columns=['Clean_DeliveryTime'])
    
    # ----------------------------------------------------------------------------------
    # 6. Save Cleaned & Enriched Output to Excel using pandas ExcelWriter
    # ----------------------------------------------------------------------------------
    print(f"\nSaving validated output to '{output_excel}' ...")
    with pd.ExcelWriter(output_excel, engine="openpyxl") as writer:
        df_export.to_excel(writer, sheet_name="Enriched_Orders", index=False)
        summary_df.to_excel(writer, sheet_name="Cuisine_Summary", index=False)
        
        # Access openpyxl workbook to style and auto-fit columns
        wb = writer.book
        
        # Style Cuisine_Summary
        ws_sum = wb["Cuisine_Summary"]
        for col in ws_sum.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = col[0].column_letter
            ws_sum.column_dimensions[col_letter].width = max(max_len + 4, 15)
            
        # Style Enriched_Orders
        ws_orders = wb["Enriched_Orders"]
        for col in ws_orders.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = col[0].column_letter
            ws_orders.column_dimensions[col_letter].width = max(max_len + 4, 14)
            
    print(f"Workbook successfully saved to: {output_excel}\n")
    
    # ----------------------------------------------------------------------------------
    # 7. Print Inspection Output to Console
    # ----------------------------------------------------------------------------------
    print("-" * 80)
    print("CORRECTED CUISINE SUMMARY TABLE:")
    print("-" * 80)
    print(summary_df.to_string(index=False))
    print("-" * 80)
    
    print("\nINSPECTION OF PREVIOUSLY CORRUPTED RECORD (ORD3005):")
    print(df_export[df_export['OrderID'] == 'ORD3005'][['OrderID', 'CustomerName', 'Cuisine', 'DeliveryTime', 'Revenue', 'PerformanceFlag']])
    
    print("\nINSPECTION OF PREVIOUSLY DROPPED RECORD (ORD3021 - Missing Cuisine):")
    print(df_export[df_export['OrderID'] == 'ORD3021'][['OrderID', 'CustomerName', 'Cuisine', 'DeliveryTime', 'Revenue', 'PerformanceFlag']])
    print("=" * 80)

if __name__ == "__main__":
    run_corrected_pipeline()
