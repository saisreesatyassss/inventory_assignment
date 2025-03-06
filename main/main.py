import pandas as pd

def find_inventory_details(sku, inventory_file, msku2sku_file):
    # Load CSV files
    inventory_df = pd.read_csv(inventory_file)
    msku2sku_df = pd.read_csv(msku2sku_file)
    
    # Find the corresponding msku for the given sku
    msku_row = msku2sku_df[msku2sku_df['sku'] == sku]
    
    if msku_row.empty:
        return "SKU not found in Msku2Skus.csv"
    
    msku = msku_row.iloc[0]['msku']
    
    # Find the product details in inventory based on msku
    product_row = inventory_df[inventory_df['msku'] == msku]
    
    if product_row.empty:
        return "Matching MSKU not found in Inventory.csv"
    
    # Return product details
    return product_row[['Product Name', 'msku', 'Opening Stock']].to_dict(orient='records')[0]

def find_combo_inventory(combo, combos_file, inventory_file):
    # Load CSV files
    combos_df = pd.read_csv(combos_file)
    inventory_df = pd.read_csv(inventory_file)
    
    # Find the row for the given combo
    combo_row = combos_df[combos_df['Combo'] == combo]
    if combo_row.empty:
        return "Combo not found in Combos.csv"
    
    # Extract SKUs from the combo row (excluding NaN values)
    skus = combo_row.iloc[0, 1:].dropna().tolist()
    
    # Find inventory details for each SKU (matching as msku)
    matching_products = inventory_df[inventory_df['msku'].isin(skus)]
    
    if matching_products.empty:
        return "No matching MSKU found in Inventory.csv"
    
    return matching_products[['Product Name', 'msku', 'Opening Stock']].to_dict(orient='records')

# Example usage
inventory_file = 'Inventory.csv'
msku2sku_file = 'Msku2Skus.csv'
combos_file = 'Combos.csv'

combo_input = input("Enter Combo: ")
result = find_combo_inventory(combo_input, combos_file, inventory_file)
print(result)
