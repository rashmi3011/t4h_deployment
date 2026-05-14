# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "6dcd6ca3-4d7f-4330-aac4-8de7ea58c9dc",
# META       "default_lakehouse_name": "Dev_lake",
# META       "default_lakehouse_workspace_id": "9dbec92e-1d0a-48bb-b603-4d72195b8acb",
# META       "known_lakehouses": [
# META         {
# META           "id": "6dcd6ca3-4d7f-4330-aac4-8de7ea58c9dc"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
