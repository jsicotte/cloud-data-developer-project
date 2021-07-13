{{ config(materialized='view') }}

select a.airport, f.cancellation_reason, count(*) as total
from airports a
join flights f on a.iata_code = f.origin_airport
where f.cancellation_reason is not null
group by 1,2