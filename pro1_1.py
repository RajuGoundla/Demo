import pandas as pd
import snowflake.connector

# Connect to Snowflake
conn = snowflake.connector.connect(
    user='Raju',
    password='7036217979@rR',
    account='iv45230.ap-south-1.aws',
    warehouse='COMPUTE_WH',
    database='PROJECT',
    schema='PRO1'
)

    # Define the file path
file_path = "C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv"

    # Read the CSV file into a DataFrame
dataframe = pd.read_csv(file_path)

    # Count the number of rows in the DataFrame
row_count = len(dataframe)

    # Print the number of rows
print("Number of rows in the DataFrame:", row_count)

    # Create a DataFrame containing the row count
row_count_df = pd.DataFrame({"RowCount": [row_count]})

    # Save the row count DataFrame as a CSV file
output_file_path = "output1.csv"
row_count_df.to_csv(output_file_path, index=False)

# Create a cursor
cursor = conn.cursor()

# Define the SQL command to create the table
create_table_sql = """
CREATE OR REPLACE TABLE row_count_table (
    row_count INTEGER
)
"""

# Execute the SQL command to create the table
cursor.execute(create_table_sql)

# Insert the count value into the target table
cursor.execute("""
    INSERT INTO row_count_table (row_count)
    VALUES (%s)
    """, (row_count,))

    # Print a message indicating successful completion
print("\nCSV file successfully created at:", row_count)

#-------------------------------------------------------------------------------------------------------------------------------------



    #filter the BOROUGH and ZIP CODE from the file
filtered_df = dataframe[dataframe['BOROUGH'].isnull() | dataframe['ZIP CODE'].isnull()]

    # Count the number of rows in the DataFrame
row_count1 = len(filtered_df)

        # Create a DataFrame containing the row count
row_count_df1 = pd.DataFrame({"RowCount": [row_count1]})

    # Save the row count DataFrame as a CSV file
output_file_path1 = "output2.csv"
row_count_df1.to_csv(output_file_path1, index=False)

print("\nCount of Missing data for Borough or Zip code:", row_count1)

