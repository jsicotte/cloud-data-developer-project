# Data Loading Script
This is a very simple script that will rebuild all the tables and import data from CSV files.

## Configuring
It is of course recommended you use a virtual env and install the required packages:
```
pip install -r requirements.txt 
```
Next you will need to configure the `settings.toml` file and specify the following:
```
database = 
schema = 
warehouse = 
airlines_path = 
airports_path = 
flight_partitions_path = 
```
Do not add rows for user, password and account credentials. To specify these values create a .secrets.toml and specify the following:
```
user = 
password = 
account = 
```
Once configuration is complete, run the script: `python LoadData.py`.
## Important Note:
Each run of this script will replace the existing tables and re-load all the data.