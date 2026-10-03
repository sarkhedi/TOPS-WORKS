"""
========================================================================================
SECTION D (STEP 1): AI-GENERATED ORIGINAL SCRIPT (UNMODIFIED)
Tool: AI Assistant (ChatGPT / Claude Promoted Prototype)
Description: Naive implementation attempting to fulfill the prompt requirements.
========================================================================================
"""

import pandas as pd
import numpy as np

def run_ai_script():
    print("Running AI Original Script...")
    
    # 1. Read food delivery orders CSV file
    df = pd.read_csv("food_orders_test_data.csv")
    
    # 2. Add PerformanceFlag (Naive binary condition: >60 is 'Delayed', else 'On Time')
    # BUG: Negative delivery time (e.g. -5) evaluates as <= 60, incorrectly marked as 'On Time'!
    df['PerformanceFlag'] = np.where(df['DeliveryTime'] > 60, 'Delayed', 'On Time')
    
    # 3. Produce summary table grouped by Cuisine
    # BUG 1: The -5 delivery time is included in the mean, severely skewing the average!
    # BUG 2: Rows with NaN Cuisine are silently dropped by groupby, losing revenue and order count!
    summary_df = df.groupby('Cuisine').agg(
        Total_Revenue=('Revenue', 'sum'),
        Average_DeliveryTime=('DeliveryTime', 'mean'),
        Order_Count=('OrderID', 'count')
    ).reset_index()
    
    # 4. Save to Excel using pandas ExcelWriter
    output_filename = "food_delivery_summary_ai.xlsx"
    with pd.ExcelWriter(output_filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="Enriched_Orders", index=False)
        summary_df.to_excel(writer, sheet_name="Cuisine_Summary", index=False)
        
    print(f"AI Original Script finished. Output saved to {output_filename}\n")
    print("AI Generated Summary Table:")
    print(summary_df)
    print("\nAI Enriched Row with DeliveryTime = -5:")
    print(df[df['DeliveryTime'] < 0][['OrderID', 'Cuisine', 'DeliveryTime', 'PerformanceFlag']])

if __name__ == "__main__":
    run_ai_script()
