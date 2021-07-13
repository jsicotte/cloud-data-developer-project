{{ config(materialized='view') }}

with origin_pairs(airline, origin_airport, destination_airport) as (
    select airline, origin_airport, destination_airport
    from flights
    group by 1, 2, 3
)
select airline, count(*) as num_routes
from origin_pairs
group by 1