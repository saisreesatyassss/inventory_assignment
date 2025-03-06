import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("Combos skus.csv", header=None)

# Remove the "Status" column (column index 15)
df = df.drop(columns=[15])

# Define the SKU columns (from SKU1 to SKU14, i.e., column indices 1 to 14)
sku_columns = list(range(1, 15))

# Remove rows where all SKU columns are empty (NaN)
df_filtered = df.dropna(subset=sku_columns, how='all')

# Save the filtered DataFrame to a new CSV file
df_filtered.to_csv("Filtered_Combos_skus.csv", index=False, header=False)

print("Filtered data saved to 'Filtered_Combos_skus.csv'")
