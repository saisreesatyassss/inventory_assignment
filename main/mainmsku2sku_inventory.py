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

# Example usage
inventory_file = 'Inventory.csv'
msku2sku_file = 'Msku2Skus.csv'
sku_input = input("Enter SKU: ")

result = find_inventory_details(sku_input, inventory_file, msku2sku_file)
print(result)
