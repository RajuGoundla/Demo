import pandas as pd

# Load the original dataset
original_df = pd.read_csv("C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv")

# Extract unique values for latitude and longitude without decimals
original_df['LATITUDE'] = original_df['LATITUDE'].fillna('').astype(str).str.split('.').str[0]
original_df['LONGITUDE'] = original_df['LONGITUDE'].fillna('').astype(str).str.split('.').str[0]

# Extract unique combinations of latitude, longitude, borough, and zip code
unique_combinations = original_df[['LATITUDE', 'LONGITUDE', 'BOROUGH', 'ZIP CODE']].dropna().drop_duplicates()

# Create a CSV file with unique values for Latitude, Longitude, Borough, and Zip codes
unique_combinations.to_csv("unique_values1.csv", index=False)

# Populate the original dataset with missing borough and zip codes
missing_data = original_df[(original_df['BOROUGH'].isnull()) | (original_df['ZIP CODE'].isnull())]
missing_data = missing_data.merge(unique_combinations, on=['LATITUDE', 'LONGITUDE'], how='left', suffixes=('_orig', '_new'))
missing_data['BOROUGH_orig'] = missing_data['BOROUGH_orig'].fillna(missing_data['BOROUGH_new'])
missing_data['ZIP CODE_orig'] = missing_data['ZIP CODE_orig'].fillna(missing_data['ZIP CODE_new'])

# Update the original dataset with corrected data
original_df.update(missing_data[['BOROUGH_orig', 'ZIP CODE_orig']])

# Final counts
count_missing = original_df['BOROUGH'].isnull().sum()
count_corrected = len(missing_data) - count_missing

print("Final count of rows with missing Borough and Zip codes:", count_missing)
print("Count of rows where missing Borough and Zip codes were added / corrected:", count_corrected)

# Save the updated dataset without missing values
original_df.dropna(subset=['BOROUGH', 'ZIP CODE', 'LATITUDE', 'LONGITUDE'], inplace=True)
original_df.to_csv("cleaned_dataset.csv", index=False)
