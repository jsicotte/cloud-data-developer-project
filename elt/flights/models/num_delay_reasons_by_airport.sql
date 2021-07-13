{{ config(materialized='view') }}

with delay_type_counts(origin_airport, destination_airport, departure_delay, arrival_delay, air_system_delay, security_delay, airline_delay, late_aircraft_delay, weather_delay) as (
    select
    origin_airport, destination_airport, departure_delay, arrival_delay,
    case when air_system_delay is not null and air_system_delay <> 0 then 1 else 0 end as air_system_delay,
    case when security_delay is not null and security_delay <> 0 then 1 else 0 end as security_delay,
    case when airline_delay is not null and airline_delay <> 0 then 1 else 0 end as airline_delay,
    case when late_aircraft_delay is not null and late_aircraft_delay <> 0 then 1 else 0 end as late_aircraft_delay,
    case when weather_delay is not null and weather_delay <> 0 then 1 else 0 end as weather_delay
    from flights
),
departure_delays(airport, air_system_delay, security_delay, airline_delay, late_aircraft_delay, weather_delay) as (
    select origin_airport as airport, sum(air_system_delay), sum(security_delay), sum(airline_delay), sum(late_aircraft_delay), sum(weather_delay)
    from delay_type_counts
    where departure_delay > 0
    group by 1
),
arrival_delays(airport, air_system_delay, security_delay, airline_delay, late_aircraft_delay, weather_delay) as (
    select destination_airport as airport, sum(air_system_delay), sum(security_delay), sum(airline_delay), sum(late_aircraft_delay), sum(weather_delay)
    from delay_type_counts
    where arrival_delay > 0
    group by 1
),
all_delays(airport, air_system_delay, security_delay, airline_delay, late_aircraft_delay, weather_delay) as (
    select airport, air_system_delay, security_delay, airline_delay, late_aircraft_delay, weather_delay
    from departure_delays
    union all
    select airport, air_system_delay, security_delay, airline_delay, late_aircraft_delay, weather_delay
    from arrival_delays
)
select airport, sum(a.air_system_delay) as num_air_system_delay, sum(a.security_delay) as num_security_delay, sum(a.airline_delay) as num_airline_delay, sum(a.late_aircraft_delay) as num_late_aircraft_delay, sum(a.weather_delay) as num_weather_delay
from all_delays a
group by 1