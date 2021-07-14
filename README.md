# Project Overview
This project provides a set of reports for Northwoods Airlines. The report visualizations are contained in a databricks notebook (see the `notebook` directory in this repo). The data that backs the visualizations is stored in Snowflake with the reporting views being populated by DBT.

# Project Setup
The `data_load` and `elt` directories contain more detailed instructions, though at a high level:
1. Load the data with a script under `data_load`.
2. Generate the database views dbt, see the `elt` directory.
3. Load the Databricks notebook into your environment. This is accomplished by simply importing the Reports.dbc file into your Databricks worksapce.