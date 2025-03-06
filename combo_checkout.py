# import pandas as pd
# import streamlit as st

# def load_data():
#     inventory_df = pd.read_csv("main/inventory.csv")
#     combos_df = pd.read_csv("main/combos.csv")
#     return inventory_df, combos_df

# def update_inventory(selected_combos, inventory_df):
#     for combo in selected_combos:
#         skus = combo['skus']
#         quantity = combo['quantity']
#         for sku in skus:
#             if sku in inventory_df['msku'].values:
#                 inventory_df.loc[inventory_df['msku'] == sku, 'Opening Stock'] -= quantity
    
#     inventory_df.to_csv("Updated_Inventory.csv", index=False)
#     return inventory_df

# def combo_checkout():
#     inventory_df, combos_df = load_data()
#     combo_options = combos_df["Combo"].unique()
    
#     selected_combos = []
    
#     st.title("Combo Checkout System")
#     combo_selected = st.selectbox("Select Combo", combo_options)
#     quantity_selected = st.number_input("Enter Quantity", min_value=1, step=1)
    
#     combo_row = combos_df[combos_df['Combo'] == combo_selected]
#     if combo_row.empty:
#         st.error("Combo not found in combos.csv")
#         return
    
#     skus = combo_row.iloc[0, 1:].dropna().values  # Extract SKUs from combo
    
#     stock_info = []
#     for sku in skus:
#         stock_row = inventory_df[inventory_df['msku'] == sku]
#         if stock_row.empty:
#             stock_info.append(f"{sku}: Not Found in Inventory")
#         else:
#             stock_available = stock_row['Opening Stock'].values[0]
#             stock_info.append(f"{sku}: {stock_available} in stock")
    
#     st.write("Current Stock Levels:")
#     for info in stock_info:
#         st.write(info)
    
#     if st.button("Add Combo"):
#         selected_combos.append({"combo": combo_selected, "skus": skus, "quantity": quantity_selected})
#         st.success(f"Added {quantity_selected} of {combo_selected}")
    
#     if st.button("Checkout"):
#         updated_inventory = update_inventory(selected_combos, inventory_df)
#         st.success("Inventory updated! Download the updated file below.")
#         csv = updated_inventory.to_csv(index=False)
#         st.download_button(label="Download Updated Inventory", data=csv, file_name="Updated_Inventory.csv", mime="text/csv")

# # Run the function if this script is executed directly
# if __name__ == "__main__":
#     combo_checkout()


import pandas as pd
import streamlit as st
from load_data import load_data
# def load_data():
#     inventory_df = pd.read_csv("main/inventory.csv")
#     combos_df = pd.read_csv("main/combos.csv")
#     return inventory_df, combos_df

def update_inventory(selected_combos, inventory_df):
    for combo in selected_combos:
        for sku in combo["skus"]:
            if sku in inventory_df['msku'].values:
                inventory_df.loc[inventory_df['msku'] == sku, 'Opening Stock'] -= combo["quantity"]
    
    inventory_df.to_csv("Updated_Inventory.csv", index=False)
    return inventory_df

def combo_checkout():
    inventory_df, combos_df = load_data()
    combo_options = combos_df["Combo"].unique()
    
    selected_combos = st.session_state.get("selected_combos", [])
    
    st.title("Combo Checkout System")
    combo_selected = st.selectbox("Select Combo", combo_options)
    quantity_selected = st.number_input("Enter Quantity", min_value=1, step=1)
    
    combo_row = combos_df[combos_df['Combo'] == combo_selected]
    if combo_row.empty:
        st.error("Combo not found in Combos.csv")
        return
    
    skus = combo_row.iloc[0, 1:].dropna().tolist()
    stock_available = {sku: inventory_df[inventory_df['msku'] == sku]['Opening Stock'].values[0] if sku in inventory_df['msku'].values else 0 for sku in skus}

    st.write("### SKUs in this Combo:")
    for sku, stock in stock_available.items():
        st.write(f"{sku}: Available - {stock}")
    
    if st.button("Add Combo"):
        selected_combos.append({"combo": combo_selected, "skus": skus, "quantity": quantity_selected})
        st.session_state["selected_combos"] = selected_combos
        st.success(f"Added {quantity_selected} of {combo_selected}")

    if st.button("Checkout"):
        updated_inventory = update_inventory(selected_combos, inventory_df)
        st.session_state["inventory_df"] = updated_inventory  # Persist the updated inventory
        st.success("Inventory updated! Download the updated file below.")
        csv = updated_inventory.to_csv(index=False)
        st.download_button(label="Download Updated Inventory", data=csv, file_name="Updated_Inventory.csv", mime="text/csv")

    # Display Updated Inventory in UI
    if "inventory_df" in st.session_state:
        st.write("### Updated Inventory:")
        st.dataframe(st.session_state["inventory_df"])

