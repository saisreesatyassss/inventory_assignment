 

# import streamlit as st
# import pandas as pd
# import io

# def load_data():
#     inventory_df = pd.read_csv("main/inventory.csv")
#     msku2sku_df = pd.read_csv("main/Msku2Skus.csv")
#     return inventory_df, msku2sku_df

# def update_inventory(selected_items, inventory_df):
#     for item in selected_items:
#         msku = item['msku']
#         quantity = item['quantity']
#         if msku in inventory_df['msku'].values:
#             inventory_df.loc[inventory_df['msku'] == msku, 'Opening Stock'] -= quantity
#     return inventory_df

# def main():
#     st.sidebar.title("Inventory Management")
    
#     inventory_df, msku2sku_df = load_data()
    
#     # Initialize session state
#     if "selected_items" not in st.session_state:
#         st.session_state.selected_items = []
    
#     sku_options = msku2sku_df["sku"].unique()
    
#     st.title("Inventory Checkout System")
#     sku_selected = st.selectbox("Select SKU", sku_options)
#     quantity_selected = st.number_input("Enter Quantity", min_value=1, step=1)
    
#     msku_row = msku2sku_df[msku2sku_df['sku'] == sku_selected]
#     if msku_row.empty:
#         st.error("SKU not found in Msku2Skus.csv")
#         return
    
#     msku = msku_row.iloc[0]['msku']
#     stock_row = inventory_df[inventory_df['msku'] == msku]
#     if stock_row.empty:
#         st.error("Matching MSKU not found in Inventory.csv")
#         return
    
#     stock_available = stock_row['Opening Stock'].values[0]
#     st.write(f"Current Stock: {stock_available}")
    
#     if st.button("Add Item"):
#         st.session_state.selected_items.append({"sku": sku_selected, "msku": msku, "quantity": quantity_selected})
#         st.success(f"Added {quantity_selected} of {sku_selected}")

#     # Display selected items
#     if st.session_state.selected_items:
#         st.subheader("Selected Items for Checkout")
#         st.table(pd.DataFrame(st.session_state.selected_items))

#     if st.button("Checkout"):
#         updated_inventory = update_inventory(st.session_state.selected_items, inventory_df)
#         st.success("Inventory updated! Download the updated file below.")
        
#         # Convert DataFrame to CSV for download
#         csv_buffer = io.StringIO()
#         updated_inventory.to_csv(csv_buffer, index=False)
#         csv_data = csv_buffer.getvalue()
        
#         # Provide download button
#         st.download_button(label="Download Updated Inventory", data=csv_data, file_name="Updated_Inventory.csv", mime="text/csv")
        
#         # Reset selected items after checkout
#         st.session_state.selected_items = []

# if __name__ == "__main__":
#     main()


import streamlit as st
import pandas as pd
from view_inventory import view_inventory
from inventory_checkout import inventory_checkout
from combo_checkout import combo_checkout

def main():
    st.sidebar.title("Inventory Management")
    page = st.sidebar.radio("Navigate", ["Home", "Inventory Checkout", "Combos Checkout","View Inventory",])
    
    if page == "Home":
        st.title("Welcome to Inventory Management System")
        st.write("Use the sidebar to navigate.")
    elif page == "Inventory Checkout":
        inventory_checkout()
    elif page == "Combos Checkout":
        combo_checkout()
    elif page == "View Inventory":
        view_inventory()

if __name__ == "__main__":
    main()
