import pandas as pd

# Step 1: Read data from a local CSV file
data = pd.read_csv('C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv') 

# Step 2: Convert the 'DATE' column to datetime
data['ACCIDENT DATE'] = pd.to_datetime(data['ACCIDENT DATE'])

# Step 3: Group by date, borough, and vehicle type, count accidents, and sort the values
grouped_data = data.groupby(['ACCIDENT DATE', 'BOROUGH', 'VEHICLE TYPE CODE 1']).size().reset_index(name='Accidents')
sorted_data = grouped_data.sort_values(by='Accidents', ascending=False)

# Step 4: Get top 5 days with maximum accidents
top_5_days = sorted_data.groupby('ACCIDENT DATE').head(5)

# Step 7: Convert date format
top_5_days['ACCIDENT DATE'] = top_5_days['ACCIDENT DATE'].dt.strftime('%d/%m/%Y')


# Rename columns as per the specified format
top_5_days_max_accidents = top_5_days.rename(columns={'ACCIDENT DATE' : 'ACCIDENT_DATE', 'BOROUGH' : 'BOROUGH',
                                                       'VEHICLE TYPE CODE 1' : 'VEHICLE_TYPE_CODE', 'Accidents' :'Accidents'})


# Step 5: Display the results
print(top_5_days[['ACCIDENT DATE', 'BOROUGH', 'VEHICLE TYPE CODE 1', 'Accidents']])

# Step 6: Save output as CSV file
top_5_days_max_accidents.to_csv('top_5_days_accidents.csv', index=False)

# Step 7: Save output as Parquet file
top_5_days_max_accidents.to_parquet('top_5_days_accidents.parquet', index=False)
