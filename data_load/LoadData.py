import snowflake.connector
import os
import logging


con = snowflake.connector.connect(
    user='jsicotte',
    password=PASSWORD,
    account=ACCOUNT,
    database=DATABASE,
    schema=SCHEMA,
    warehouse=WAREHOUSE
)


#con.cursor().execute("PUT file:///Users/jsicotte/Documents/workspaces/cloud-data-developer-project/airlines.csv @%airlines")
#con.cursor().execute("COPY INTO airlines")

# con.cursor().execute("create or replace stage airports")
# con.cursor().execute("PUT file:///Users/jsicotte/Documents/workspaces/cloud-data-developer-project/airports.csv @%airports")
# con.cursor().execute("COPY INTO airports file_format = (type = csv skip_header = 1)")


sql = """

CREATE TABLE "AIRLINES"."PUBLIC"."FLIGHTS" (
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

con.cursor().execute(sql)
con.cursor().execute("create or replace stage flights")
con.cursor().execute("PUT file:///Users/jsicotte/Documents/workspaces/cloud-data-developer-project/flights/partition-* @%flights")
con.cursor().execute("COPY INTO flights file_format = (type = csv skip_header = 1)")
con.close()