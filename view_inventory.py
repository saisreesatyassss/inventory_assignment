# # import pandas as pd
# # import streamlit as st

# # def load_data():
# #     inventory_file = "main/inventory.csv"
# #     msku2sku_file = "main/Msku2Skus.csv"
    
# #     inventory_df = pd.read_csv(inventory_file)
# #     msku2sku_df = pd.read_csv(msku2sku_file)
    
# #     return inventory_df, msku2sku_df

# # def view_inventory():
# #     st.title("View Inventory")
# #     inventory_df, _ = load_data()
# #     st.dataframe(inventory_df)


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# def load_data():
#     inventory_file = "main/inventory.csv"
#     msku2sku_file = "main/Msku2Skus.csv"
    
#     inventory_df = pd.read_csv(inventory_file)
#     msku2sku_df = pd.read_csv(msku2sku_file)
    
#     return inventory_df, msku2sku_df

# def view_inventory():
#     st.title("📦 Inventory Overview")
#     inventory_df, _ = load_data()
    
#     # Display inventory dataframe
#     st.subheader("Inventory Data")
#     st.dataframe(inventory_df)
    
#     # Summary Statistics
#     total_items = len(inventory_df)
#     in_stock_count = (inventory_df["Opening Stock"] > 0).sum()
#     out_of_stock_count = (inventory_df["Opening Stock"] == 0).sum()
    
#     st.subheader("Inventory Summary")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Items", total_items)
#     col2.metric("In Stock", in_stock_count)
#     col3.metric("Out of Stock", out_of_stock_count)
    
#     # Bar Chart for Stock Levels
#     st.subheader("Stock Levels")
#     fig = px.bar(inventory_df, x="Product Name", y="Opening Stock", 
#                  color="Opening Stock", title="Stock Availability",
#                  labels={'Opening Stock': 'Stock Quantity'},
#                  height=500)
#     st.plotly_chart(fig)
    
#     # Display out-of-stock items
#     out_of_stock_items = inventory_df[inventory_df["Opening Stock"] == 0]
#     if not out_of_stock_items.empty:
#         st.subheader("⚠️ Out of Stock Items")
#         st.dataframe(out_of_stock_items)


import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(uploaded_file=None):
    if uploaded_file is not None:
        inventory_df = pd.read_csv(uploaded_file)
    else:
        inventory_file = "main/inventory.csv"
        inventory_df = pd.read_csv(inventory_file)
    return inventory_df

def validate_data(df):
    required_columns = {"Product Name", "msku", "Opening Stock"}
    if not required_columns.issubset(df.columns):
        st.error("Uploaded file is missing required columns: Product Name, msku, Opening Stock")
        return False
    return True

def view_inventory():
    st.title("📦 Inventory Overview")
    
    uploaded_file = st.file_uploader("Upload Inventory CSV", type=["csv"])
    inventory_df = load_data(uploaded_file)
    
    if not validate_data(inventory_df):
        return
    
    # Display inventory dataframe
    st.subheader("Inventory Data")
    st.dataframe(inventory_df)
    
    # Summary Statistics
    total_items = len(inventory_df)
    in_stock_count = (inventory_df["Opening Stock"] > 0).sum()
    out_of_stock_count = (inventory_df["Opening Stock"] == 0).sum()
    
    st.subheader("Inventory Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Items", total_items)
    col2.metric("In Stock", in_stock_count)
    col3.metric("Out of Stock", out_of_stock_count)
    
    # Bar Chart for Stock Levels
    st.subheader("Stock Levels")
    fig = px.bar(inventory_df, x="Product Name", y="Opening Stock", 
                 color="Opening Stock", title="Stock Availability",
                 labels={'Opening Stock': 'Stock Quantity'},
                 height=500)
    st.plotly_chart(fig)
    
    # Display out-of-stock items
    out_of_stock_items = inventory_df[inventory_df["Opening Stock"] == 0]
    if not out_of_stock_items.empty:
        st.subheader("⚠️ Out of Stock Items")
        st.dataframe(out_of_stock_items)

 