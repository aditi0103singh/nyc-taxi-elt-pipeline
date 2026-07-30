{{
    config(
        materialized='incremental',
        unique_key='trip_id'
    )
}}

select
    md5(cast(coalesce(vendor_id, '') as varchar) || '-' || cast(pickup_datetime as varchar)) as trip_id,
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    pickup_location_id,
    dropoff_location_id,
    passenger_count,
    trip_distance,
    trip_duration_minutes,
    average_speed_mph,
    fare_amount,
    tip_amount,
    total_amount,
    tip_percentage
from {{ ref('int_taxi_trip_metrics') }}

{% if is_incremental() %}
    -- Only process new trips that occurred after the latest pickup_datetime in the existing table
    where pickup_datetime > (select max(pickup_datetime) from {{ this }})
{% endif %}