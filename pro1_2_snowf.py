import pandas as pd
import os
import snowflake.connector
from snowflake.snowpark.session import Session
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import *

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='Raju',
    password='7036217979@rR',
    account='iv45230.ap-south-1.aws',
    warehouse='COMPUTE_WH',  # Replace <COMPUTE_WH> with your warehouse name
    database='PROJECT',       # Replace <PROJECT> with your database name
    schema='PRO2'             # Replace <PRO2> with your schema name
)

cursor = conn.cursor()


# Create a cursor object
cursor = conn.cursor()

tableName = 'PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS'
tableName1 = 'PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS'


# Step 1: Extract Unique Combinations of Latitude, Longitude, Borough, and Zip Code
# Step 1: Extract Unique Combinations of Latitude, Longitude, Borough, and Zip Code
sql_extract_unique = """
SELECT DISTINCT LATITUDE, LONGITUDE, BOROUGH, ZIP_CODE
FROM {}
WHERE LATITUDE IS NOT NULL AND LONGITUDE IS NOT NULL
""".format(tableName)

cursor.execute(sql_extract_unique)
unique_combinations = cursor.fetchall()

# Step 2: Create a CSV File with Unique Combinations
with open('unique_coordinates.csv', 'w') as f:
    f.write("LATITUDE,LONGITUDE,BOROUGH,ZIP_CODE\n")
    for row in unique_combinations:
        f.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")

# Step 3: Stage CSV File in Snowflake
cursor.execute("PUT file:///C:/Users/hp/Desktop/project/unique_coordinates.csv @PRO2")

# Step 4: Update the Original Dataset
sql_update_dataset = """
UPDATE PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS1 AS original_dataset
SET BOROUGH = new_data.BOROUGH, ZIP_CODE = new_data.ZIP_CODE
FROM (
    SELECT LATITUDE, LONGITUDE, BOROUGH, ZIP_CODE
    FROM unique_coordinates
) AS new_data
WHERE original_dataset.LATITUDE = new_data.LATITUDE
  AND original_dataset.LONGITUDE = new_data.LONGITUDE
  AND (original_dataset.BOROUGH IS NULL OR original_dataset.ZIP_CODE IS NULL)
"""


cursor.execute(sql_update_dataset)

# Step 4: Calculate Counts
sql_counts = """
SELECT 
    COUNT(*) AS missing_values_count,
    SUM(CASE WHEN PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS1.BOROUGH IS NULL OR PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS1.ZIP_CODE IS NULL THEN 1 ELSE 0 END) AS missing_values_updated_count
FROM PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS1
"""

cursor.execute(sql_counts)
counts_result = cursor.fetchone()

missing_values_count = counts_result[0]
missing_values_updated_count = counts_result[1]

print("Final count of rows with missing Borough and Zip Code values:", missing_values_count)
print("Count of rows where missing Borough and Zip Code values were added or corrected:", missing_values_updated_count)




# Close the cursor and connection
cursor.close()
conn.close()