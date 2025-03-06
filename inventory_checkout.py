import pandas as pd
import streamlit as st

def load_data():
    inventory_df = pd.read_csv ("main/inventory.csv")
    msku2sku_df = pd.read_csv("main/Msku2Skus.csv")
    return inventory_df, msku2sku_df

def update_inventory(selected_items, inventory_df):
    for item in selected_items:
        msku = item['msku']
        quantity = item['quantity']
        if msku in inventory_df['msku'].values:
            inventory_df.loc[inventory_df['msku'] == msku, 'Opening Stock'] -= quantity
    inventory_df.to_csv("Updated_Inventory.csv", index=False)
    return inventory_df

def inventory_checkout():
    inventory_df, msku2sku_df = load_data()
    sku_options = msku2sku_df["sku"].unique()
    
    selected_items = []
    
    st.title("Inventory Checkout System")
    sku_selected = st.selectbox("Select SKU", sku_options)
    quantity_selected = st.number_input("Enter Quantity", min_value=1, step=1)
    
    msku_row = msku2sku_df[msku2sku_df['sku'] == sku_selected]
    if msku_row.empty:
        st.error("SKU not found in Msku2Skus.csv")
        return
    
    msku = msku_row.iloc[0]['msku']
    stock_row = inventory_df[inventory_df['msku'] == msku]
    if stock_row.empty:
        st.error("Matching MSKU not found in Inventory.csv")
        return
    
    stock_available = stock_row['Opening Stock'].values[0]
    st.write(f"Current Stock: {stock_available}")
    
    if st.button("Add Item"):
        selected_items.append({"sku": sku_selected, "msku": msku, "quantity": quantity_selected})
        st.success(f"Added {quantity_selected} of {sku_selected}")
    
    if st.button("Checkout"):
        updated_inventory = update_inventory(selected_items, inventory_df)
        st.success("Inventory updated! Download the updated file below.")
        csv = updated_inventory.to_csv(index=False)
        st.download_button(label="Download Updated Inventory", data=csv, file_name="Updated_Inventory.csv", mime="text/csv")


