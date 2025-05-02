import pandas as pd

# Step 1: Read data from a local CSV file
data = pd.read_csv('C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv', error_bad_lines=False)

# Step 2: Drop rows with missing values in the "VEHICLE TYPE CODE 1" column
data = data.dropna(subset=['VEHICLE TYPE CODE 1'])

# Step 4: Group by vehicle type (Code 1), count accidents, and sort the values
vehicle_type_counts = data['VEHICLE_TYPE_CODE_1'].value_counts().reset_index(name='Accidents')
vehicle_type_counts.columns = ['Vehicle_Type', 'Accidents']

# Step 5: Get top 5 vehicle types with maximum accidents
top_5_vehicle_types = vehicle_type_counts.head(5)

# Step 6: Display the results
print("Top 5 Vehicle Types Involved in Maximum Accidents:")
print(top_5_vehicle_types)

# Step 7: Save output as CSV file
top_5_vehicle_types.to_csv('top_5_vehicle_types_max_accidents.csv', index=False)

# Step 8: Save output as Parquet file
top_5_vehicle_types.to_parquet('top_5_vehicle_types_max_accidents.parquet', index=False)
