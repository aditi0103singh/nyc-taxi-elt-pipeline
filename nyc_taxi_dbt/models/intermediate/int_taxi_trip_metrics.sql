with staging as (
select * from {{ ref('stg_taxi_trips') }}
),

calculated as (
select
vendor_id,
pickup_datetime,
dropoff_datetime,
pickup_location_id,
dropoff_location_id,
passenger_count,
trip_distance,
fare_amount,
tip_amount,
total_amount,

-- Derived business metrics (DuckDB timestamp difference in minutes)
        date_diff('minute', pickup_datetime, dropoff_datetime) as trip_duration_minutes,
        
        -- Guard against division by zero for speed calculation
        case 
            when date_diff('minute', pickup_datetime, dropoff_datetime) > 0 
            then (trip_distance / (date_diff('minute', pickup_datetime, dropoff_datetime) / 60.0))
            else 0 
        end as average_speed_mph,

        -- Tip percentage calculation
        case 
            when fare_amount > 0 
            then (tip_amount / fare_amount) * 100.0 
            else 0 
        end as tip_percentage

    from staging
    from staging
    where trip_distance > 0 
      and fare_amount >= 0
      and dropoff_datetime > pickup_datetime  -- Ensures no zero-duration or backward tripswhere trip_distance > 0 
      and fare_amount >= 0
      and dropoff_datetime >= pickup_datetime
)

select * from calculated