import os
import duckdb

def main():
    # Define explicit paths based on your correct file name and location
    db_dir = "warehouse"
    db_path = os.path.join(db_dir, "warehouse.duckdb")
    parquet_path = "data/landing/yellow_tripdata_2023-01.parquet"

    # Ensure the warehouse directory exists
    os.makedirs(db_dir, exist_ok=True)

    print("Connecting to DuckDB...")
    conn = duckdb.connect(db_path)

    try:
        print("Creating schema 'raw_staging'...")
        conn.execute("CREATE SCHEMA IF NOT EXISTS raw_staging;")

        print(f"Loading Parquet file from '{parquet_path}' into raw_staging.raw_trips...")
        
        # Execute the table creation from the parquet file
        query = f"CREATE OR REPLACE TABLE raw_staging.raw_trips AS SELECT * FROM read_parquet('{parquet_path}');"
        conn.execute(query)

        # Verify the ingestion row count
        result = conn.execute("SELECT COUNT(*) FROM raw_staging.raw_trips;").fetchone()
        print(f"Success! Loaded {result[0]:,} rows into raw_staging.raw_trips.")

    except Exception as e:
        print(f"An error occurred during ingestion: {e}")
    finally:
        conn.close()
        print("DuckDB connection closed.")

if __name__ == "__main__":
    main()