{{ config(materialized='view') }}

with totals as (
    select a.airline, count(*) as total from airlines a
    join flights f on f.airline = a.iata_code1
    group by 1
),
delays as (
    select a.airline, count(*) as on_time from airlines a
    join flights f on f.airline = a.iata_code1
    where airline_delay = 0
    group by 1
)
select (to_double(d.on_time) / to_double(t.total)) as percent_on_time, d.airline
from totals t
join delays d on d.airline = t.airline