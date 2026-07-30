select *
from {{ ref('stg_taxi_trips') }}
where dropoff_datetime < pickup_datetime