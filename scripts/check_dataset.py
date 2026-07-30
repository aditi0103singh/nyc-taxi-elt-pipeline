import pandas as pd
from pathlib import Path

# Dataset path
file_path = Path("data/landing/yellow_tripdata_2023-01.parquet")

# Check if file exists
if not file_path.exists():
    print("❌ Dataset not found!")
    exit()

# Read parquet file
df = pd.read_parquet(file_path)

print("=" * 60)
print("NYC Taxi Dataset Verification")
print("=" * 60)

print(f"\nRows: {len(df):,}")
print(f"Columns: {len(df.columns)}")

print("\nColumn Names:")
for column in df.columns:
    print(f"- {column}")

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Records:")
print(df.head())