import pandas as pd

# Read the CSV file
df = pd.read_csv("Msku With Skus.csv")

# Keep only 'sku' and 'msku' columns
df = df[['sku', 'msku']]

# Save the cleaned data to a new CSV file
df.to_csv("Cleaned_Msku_With_Skus.csv", index=False)

print("Cleaned data saved to 'Cleaned_Msku_With_Skus.csv'")
