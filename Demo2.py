import pandas as pd

original_df = pd.read_csv('C:\\Users\\hp\\Desktop\\Project_Data\\Dataset_1\\nypd-motor-vehicle-collisions.csv')


# Step 1: Extract unique combinations of Latitude, Longitude, Borough, and Zip Code
#unique_df = original_df[['LATITUDE', 'LONGITUDE']].dropna().drop_duplicates().astype(int).original_df[['BOROUGH', 'ZIP CODE']].dropna().drop_duplicates()

# Selecting and processing numerical columns

unique_latitudes = original_df['LATITUDE'].dropna().unique().astype(int)
unique_longitudes = original_df['LONGITUDE'].dropna().unique().astype(int)

# Create DataFrames for latitude and longitude
latitudes_df = pd.DataFrame({'LATITUDE': unique_latitudes})
longitudes_df = pd.DataFrame({'LONGITUDE': unique_longitudes})

non_numeric_df = original_df[['BOROUGH', 'ZIP CODE']].dropna().drop_duplicates()


# Combine both DataFrames horizontally
combined_df = pd.concat([latitudes_df, longitudes_df,non_numeric_df], axis=1)


#numeric_df = original_df[['LATITUDE', 'LONGITUDE']].dropna().unique()
#numeric_df[['LATITUDE', 'LONGITUDE']] = numeric_df[['LATITUDE', 'LONGITUDE']].astype(int)

# Selecting and processing non-numerical columns
#non_numeric_df = original_df[['BOROUGH', 'ZIP CODE']].dropna().drop_duplicates()

# Concatenating the two dataframes
#unique_df = pd.concat([numeric_df, non_numeric_df], axis=1)


# Step 2: Filter out rows with missing Latitude or Longitude values
unique_df = combined_df[(combined_df['LATITUDE'] != 0) & (combined_df['LONGITUDE'] != 0)]

# Step 3: Save unique combinations to a CSV file
unique_df.to_csv('unique_coordinates2.csv', index=False)

# Step 4: Use the unique coordinates CSV file to populate the original dataset
unique_coordinates = pd.read_csv('unique_coordinates2.csv')

# Merge unique coordinates with the original dataset to populate missing values
merged_df = original_df.merge(unique_coordinates, on=['LATITUDE', 'LONGITUDE'], how='left', suffixes=('', '_new'))

# Update missing Borough and Zip Code values in the original dataset
merged_df['BOROUGH'] = merged_df['BOROUGH_new'].fillna(merged_df['BOROUGH'])
merged_df['ZIP CODE'] = merged_df['ZIP CODE_new'].fillna(merged_df['ZIP CODE'])

# Step 5: Count rows with missing Borough and Zip codes before and after population
before_population = merged_df['BOROUGH'].isna().sum()
after_population = merged_df['BOROUGH'].isna().sum()
rows_added_or_corrected = after_population - before_population

# Step 6: Save the updated dataset
merged_df.to_csv('updated_dataset.csv', index=False)

# Step 7: Print the counts
print("Before Population:")
print(f"Rows with missing Borough and Zip codes: {before_population}")

print("\nAfter Population:")
print(f"Rows with missing Borough and Zip codes: {after_population}")
print(f"Rows added or corrected: {rows_added_or_corrected}")
