{{
    config(
        materialized='table'
    )
}}

select
    cast(pickup_datetime as date) as trip_date,
    vendor_id,
    count(*) as total_trips,
    sum(passenger_count) as total_passengers,
    sum(trip_distance) as total_distance_traveled,
    avg(trip_duration_minutes) as avg_trip_duration_minutes,
    sum(fare_amount) as total_fare_revenue,
    sum(tip_amount) as total_tips_collected,
    sum(total_amount) as total_overall_revenue,
    avg(tip_percentage) as average_tip_percentage
from {{ ref('int_taxi_trip_metrics') }}
group by 1, 2
order by trip_date desc