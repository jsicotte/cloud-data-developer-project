import snowflake.connector
import os
import logging
from dynaconf import Dynaconf
from config.config import settings


con = snowflake.connector.connect(
    user=settings.user,
    password=settings.password,
    account=settings.account,
    database=settings.database,
    schema=settings.schema,
    warehouse=settings.warehouse
)

airlines_path = settings.airlines_path
airports_path = settings.airports_path
flight_partitions_path = settings.flight_partitions_path

airlines_ddl = """
create or replace TABLE AIRLINES (
	IATA_CODE1 VARCHAR(16777216) NOT NULL,
	AIRLINE VARCHAR(16777216) NOT NULL
);
"""

con.cursor().execute(airlines_ddl)
con.cursor().execute("create or replace stage airlines")
con.cursor().execute(f"PUT file://{airlines_path} @%airlines")
con.cursor().execute("COPY INTO airlines file_format = (type = csv skip_header = 1)")

airports_ddl = """
create or replace TABLE AIRPORTS (
	IATA_CODE VARCHAR(16777216) NOT NULL,
	AIRPORT VARCHAR(16777216) NOT NULL,
	CITY VARCHAR(16777216) NOT NULL,
	STATE VARCHAR(16777216) NOT NULL,
	COUNTRY VARCHAR(16777216) NOT NULL,
	LATITUDE NUMBER(8,5),
	LONGITUDE NUMBER(8,5)
);
"""

con.cursor().execute(airports_ddl)
con.cursor().execute("create or replace stage airports")
con.cursor().execute(f"PUT file://{airports_path} @%airports")
con.cursor().execute("COPY INTO airports file_format = (type = csv skip_header = 1)")


flights_ddl = """
create or replace TABLE "AIRLINES"."PUBLIC"."FLIGHTS" (
YEAR NUMBER,
MONTH NUMBER,
DAY NUMBER,
DAY_OF_WEEK NUMBER,
AIRLINE STRING,
FLIGHT_NUMBER STRING,
TAIL_NUMBER  STRING,
ORIGIN_AIRPORT  STRING,
DESTINATION_AIRPORT STRING,
SCHEDULED_DEPARTURE STRING,
DEPARTURE_TIME STRING,
DEPARTURE_DELAY NUMBER,
TAXI_OUT NUMBER,
WHEELS_OFF STRING,
SCHEDULED_TIME NUMBER,
ELAPSED_TIME NUMBER,
AIR_TIME NUMBER,
DISTANCE NUMBER,
WHEELS_ON NUMBER,
TAXI_IN NUMBER,
SCHEDULED_ARRIVAL NUMBER,
ARRIVAL_TIME STRING,
ARRIVAL_DELAY STRING,
DIVERTED NUMBER,
CANCELLED NUMBER,
CANCELLATION_REASON STRING,
AIR_SYSTEM_DELAY NUMBER,
SECURITY_DELAY NUMBER,
AIRLINE_DELAY NUMBER,
LATE_AIRCRAFT_DELAY NUMBER,
WEATHER_DELAY NUMBER
);
"""

con.cursor().execute(flights_ddl)
con.cursor().execute("create or replace stage flights")
con.cursor().execute(f"PUT file://{flight_partitions_path}partition-* @%flights")
con.cursor().execute("COPY INTO flights file_format = (type = csv skip_header = 1)")
con.close()