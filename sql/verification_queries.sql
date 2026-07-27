-- 1. Check total number of rows in the staging table
SELECT COUNT(*) AS total_rows 
FROM raw_staging.raw_trips;

-- 2. Inspect table schema and column data types
DESCRIBE raw_staging.raw_trips;

-- 3. Preview the first 5 records
SELECT * 
FROM raw_staging.raw_trips 
LIMIT 5;

-- 4. Basic analytical check: Average trip distance and fare amount
SELECT 
    COUNT(*) AS trip_count,
    AVG(trip_distance) AS avg_trip_distance,
    AVG(fare_amount) AS avg_fare_amount
FROM raw_staging.raw_trips;