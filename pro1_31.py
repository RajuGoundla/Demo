import pandas as pd

# Step 1: Read data from a local CSV file
data = pd.read_csv('C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv') 

# Step 2: Convert the 'DATE' column to datetime
data['ACCIDENT DATE'] = pd.to_datetime(data['ACCIDENT DATE'])

# Step 3: Group by borough and date, count accidents, and sort the values
grouped_data = data.groupby(['BOROUGH', 'ACCIDENT DATE']).size().reset_index(name='Accidents')

# Step 4: Find the borough with maximum accidents
max_accidents_borough = grouped_data.groupby('BOROUGH')['Accidents'].sum().idxmax()

# Step 5: Filter the data for the borough with maximum accidents
max_accidents_borough_data = grouped_data[grouped_data['BOROUGH'] == max_accidents_borough]

# Step 6: Sort by accidents count and get top 5 days
top_5_days_max_accidents = max_accidents_borough_data.sort_values(by='Accidents', ascending=False).head(5)

top_5_days_max_accidents['ACCIDENT DATE'] = top_5_days_max_accidents['ACCIDENT DATE'].dt.strftime('%d/%m/%Y')


# Rename columns as per the specified format
top_5_days_max_accidents = top_5_days_max_accidents.rename(columns={'BOROUGH': 'BOROUGH', 
                                                                    'ACCIDENT DATE': 'ACCIDENT_DATE', 'Accidents': 'Accidents'})


# Step 7: Display the results
print("Borough with Maximum Accidents:", max_accidents_borough)
print("Top 5 Days with Maximum Accidents in", max_accidents_borough, ":")
print(top_5_days_max_accidents[['ACCIDENT_DATE', 'Accidents']])

# Step 8: Save output as CSV file
top_5_days_max_accidents.to_csv('top_5_days_max_accidents.csv', index=False)

# Step 9: Save output as Parquet file
top_5_days_max_accidents.to_parquet('top_5_days_max_accidents.parquet', index=False)
