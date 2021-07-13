{{ config(materialized='view') }}


select a.airport, f.year, f.month, count(*) as total_flights
from airports a
join flights f on (a.iata_code = f.destination_airport or a.iata_code = f.origin_airport)
group by 1,2,3


