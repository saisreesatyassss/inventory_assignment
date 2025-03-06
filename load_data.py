import os
import pandas as pd
import streamlit as st

def load_data():
    inventory_path = "main/inventory.csv"
    combos_path = "main/combos.csv"
    
    inventory_df, combos_df = None, None
    
    # Check if inventory.csv exists
    if os.path.exists(inventory_path):
        inventory_df = pd.read_csv(inventory_path)
    else:
        st.warning("⚠️ inventory.csv not found. Please upload the file.")
        uploaded_inventory = st.file_uploader("Upload inventory.csv", type="csv", key="inventory")
        if uploaded_inventory is not None:
            inventory_df = pd.read_csv(uploaded_inventory)
            inventory_df.to_csv(inventory_path, index=False)  # Save uploaded file

    # Check if combos.csv exists
    if os.path.exists(combos_path):
        combos_df = pd.read_csv(combos_path)
    else:
        st.warning("⚠️ combos.csv not found. Please upload the file.")
        uploaded_combos = st.file_uploader("Upload combos.csv", type="csv", key="combos")
        if uploaded_combos is not None:
            combos_df = pd.read_csv(uploaded_combos)
            combos_df.to_csv(combos_path, index=False)  # Save uploaded file

    # If files are missing and not uploaded, return empty dataframes
    if inventory_df is None:
        inventory_df = pd.DataFrame(columns=["Product Name", "msku", "Opening Stock"])
    if combos_df is None:
        combos_df = pd.DataFrame(columns=["Combo"] + [f"SKU{i}" for i in range(1, 15)])

    return inventory_df, combos_df
