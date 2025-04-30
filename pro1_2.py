import pandas as pd

# Step 1: Read data from a local CSV file
data = pd.read_csv('C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv') 

# Step 2: Extract Unique Combinations of Latitude, Longitude, Borough, and Zip Code
unique_combinations = data.dropna(subset=['LATITUDE', 'LONGITUDE']).drop_duplicates(subset=['LATITUDE', 'LONGITUDE', 'BOROUGH', 'ZIP CODE'])


# Step 3: Round Latitude and Longitude values
unique_combinations['LATITUDE'] = unique_combinations['LATITUDE'].round().astype(int)
unique_combinations['LONGITUDE'] = unique_combinations['LONGITUDE'].round().astype(int)

unique_combinations.to_csv('updated_dataset1.csv', index=False)

# Step 3: Merge the original dataset with the unique combinations to update missing values
merged_data = pd.merge(data, unique_combinations[['LATITUDE', 'LONGITUDE', 'BOROUGH', 'ZIP CODE']], 
                       on=['LATITUDE', 'LONGITUDE'], how='left', suffixes=('_original', '_updated'))

# Step 4: Update missing values in the original dataset
merged_data['BOROUGH'] = merged_data['BOROUGH_updated'].fillna(merged_data['BOROUGH_original'])
merged_data['ZIP CODE'] = merged_data['ZIP CODE_updated'].fillna(merged_data['ZIP CODE_original'])

# Step 5: Save the updated dataset if needed
merged_data.to_csv('updated_dataset.csv', index=False)

# Step 6: Calculate Counts
missing_values_count = merged_data[['BOROUGH', 'ZIP CODE']].isnull().any(axis=1).sum()
missing_values_updated_count = len(unique_combinations)

print("Final count of rows with missing Borough and Zip Code values:", missing_values_count)
print("Count of rows where missing Borough and Zip Code values were added or corrected:", missing_values_updated_count)
