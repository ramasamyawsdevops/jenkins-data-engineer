import pandas as pd

print("Validation Started")

df = pd.read_csv("output/result.csv")

# Check null values
if df.isnull().sum().sum() > 0:
    raise Exception("Validation Failed - Null Values Found")

# Check row count
if len(df) == 0:
    raise Exception("Validation Failed - Empty File")

print("Validation Successful")