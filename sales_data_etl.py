import pandas as pd
import os

print("ETL Started")

# Read CSV
df = pd.read_csv("input/sales_data.csv")

# Create total column
df["total"] = df["qty"] * df["price"]

# Create output folder
os.makedirs("output", exist_ok=True)

# Save output
df.to_csv("output/result.csv", index=False)

print(df)

print("ETL Completed")