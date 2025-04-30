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

# Create a cursor object
cursor = conn.cursor()



# Your Snowpark code here
tableName = 'PROJECT.PRO2.MOTOR_VEHICLE_COLLISIONS'

cursor.execute(f"SELECT COUNT(*) FROM {tableName}")

# Fetch the result of the query
count_result = cursor.fetchone()

# Extract the count value from the result
count_rows = count_result[0]

# Print the count of rows to standard output
print("The number of rows is:", count_rows)

# Create the target table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS OUTPUT_TABLE (
    COUNT_ROWS INT
)
""")

# Insert the count value into the target table
cursor.execute("""
INSERT INTO OUTPUT_TABLE (COUNT_ROWS)
VALUES (%s)
""", (count_rows,))

# Execute a SQL query to count the number of rows in the table
dataframe = cursor.table(tableName)

cursor.execute(f"SELECT COUNT(*) FROM {tableName} WHERE \"BOROUGH\" IS NULL OR \"ZIP_CODE\" IS NULL")

count_result1 = cursor.fetchone()

# Extract the count value from the result
count_rows1 = count_result1[0]


 # Print the total number of rows with missing data
print("Total number of rows with missing Borough or Zip code:", count_result1)

# Create the target table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS OUTPUT_TABLE2 (
    COUNT_ROWS INT
)
""")

# Insert the count value into the target table
cursor.execute("""
INSERT INTO OUTPUT_TABLE2 (COUNT_ROWS)
VALUES (%s)
""", (count_rows1,))





# Commit the transaction
#conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
