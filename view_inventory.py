import pandas as pd
import streamlit as st

def load_data():
    inventory_file = "main/inventory.csv"
    msku2sku_file = "main/Msku2Skus.csv"
    
    inventory_df = pd.read_csv(inventory_file)
    msku2sku_df = pd.read_csv(msku2sku_file)
    
    return inventory_df, msku2sku_df

def view_inventory():
    st.title("View Inventory")
    inventory_df, _ = load_data()
    st.dataframe(inventory_df)
