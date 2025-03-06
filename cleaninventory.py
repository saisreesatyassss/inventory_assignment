import pandas as pd

# # Load and clean Combos file
# combos_file = "Combos skus.csv"
# df_combos = pd.read_csv(combos_file)
# df_combos = df_combos.iloc[:, :5]  # Keeping only relevant columns (Combo and SKU1 to SKU4)
# df_combos.to_csv("Cleaned_Combos.csv", index=False)

# # Load and clean Msku file
# msku_file = "Msku With Skus.csv"
# df_msku = pd.read_csv(msku_file, usecols=[0, 1])  # Keep only first two columns (msku, SKU)
# df_msku.to_csv("Cleaned_Msku.csv", index=False)

# Load and clean Inventory file
inventory_file = "Current Inventory.csv"
df_inventory = pd.read_csv(inventory_file, usecols=[0, 1, 2])  # Keep only Product Name, msku, and Opening Stock
df_inventory.to_csv("Cleaned_Inventory.csv", index=False)

print("All files cleaned and saved.")

