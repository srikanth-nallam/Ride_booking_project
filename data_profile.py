import pandas as pd

# 1. Load the raw dataset
file_path = "raw_data.csv"
df = pd.read_csv(file_path)

# 2. Basic overview
print("Shape (rows, columns):", df.shape)
print("\nFirst 5 rows:")
print(df.head())

# 3. Missing values per column
print("\nMissing values per column:")
print(df.isna().sum().sort_values(ascending=False))

# 4. Exact duplicate rows
print("\nExact duplicate rows:", df.duplicated().sum())

# 5. Duplicate ride IDs
print("Duplicate ride_id values:", df["ride_id"].duplicated().sum())

# 6. Invalid values
print("Negative distances:", (df["distance_km"] < 0).sum())
print("Negative fares:", (df["fare_amount"] < 0).sum())
print("Unknown statuses:", (df["ride_status"] == "UNKNOWN_STATUS").sum())

# 7. Save a profiling report
report = pd.DataFrame({
    "column": df.columns,
    "missing_values": [df[col].isna().sum() for col in df.columns],
    "missing_percent": [round(df[col].isna().mean() * 100, 2) for col in df.columns],
    "data_type": [str(df[col].dtype) for col in df.columns],
    "distinct_values": [df[col].nunique(dropna=True) for col in df.columns],
})
report.to_csv("ride_data_quality_profile.csv", index=False)
print("\nSaved: ride_data_quality_profile.csv")
