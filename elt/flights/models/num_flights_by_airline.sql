{{ config(materialized='view') }}


select a.airline, f.month, f.year, count(*) as total_flights from flights f
join airlines a on a.IATA_CODE1 = f.airline
group by 1,2,3 


