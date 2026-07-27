import duckdb

# Connect to your warehouse
conn = duckdb.connect("warehouse/warehouse.duckdb")

# 1. Verify row count matches the success message
row_count = conn.execute("SELECT COUNT(*) FROM raw_staging.raw_trips;").fetchone()[0]
print(f"Total Rows in Warehouse: {row_count:,}")

# 2. Preview the columns and data types
print("\nTable Schema:")
schema = conn.execute("DESCRIBE raw_staging.raw_trips;").fetchall()
for col in schema[:5]:  # Print first 5 columns
    print(f" - {col[0]}: {col[1]}")

# 3. Preview actual data rows
print("\nData Preview (Top 3 rows):")
preview = conn.execute("SELECT tpep_pickup_datetime, trip_distance, fare_amount FROM raw_staging.raw_trips LIMIT 3;").fetchdf()
print(preview)

conn.close()