{{ config(materialized='view') }}


select a.airline, count(*) as total_delays
from flights f
join airlines a on a.iata_code1 = f.airline
where f.airline_delay > 0
group by 1

