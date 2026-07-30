with source as (
    select * from {{ source('raw_staging', 'raw_trips') }}
),

renamed as (
    select
        -- identifiers & keys
        cast(VendorID as varchar) as vendor_id,
        cast(PULocationID as integer) as pickup_location_id,
        cast(DOLocationID as integer) as dropoff_location_id,
        
        -- timestamps
        cast(tpep_pickup_datetime as timestamp) as pickup_datetime,
        cast(tpep_dropoff_datetime as timestamp) as dropoff_datetime,
        
        -- metrics & details
        cast(passenger_count as integer) as passenger_count,
        cast(trip_distance as double) as trip_distance,
        cast(fare_amount as double) as fare_amount,
        cast(tip_amount as double) as tip_amount,
        cast(total_amount as double) as total_amount

    from source
)

select * from renamed