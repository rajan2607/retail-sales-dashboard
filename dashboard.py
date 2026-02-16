import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

# Load data
conn = sqlite3.connect("sales.db", check_same_thread=False)

df = pd.read_sql("SELECT * FROM sales", conn)
df["revenue"] = df["price"] * df["quantity"]

st.title("📊 Retail Sales Performance Dashboard")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"₹{df['revenue'].sum():,.0f}")
col2.metric("Total Orders", df["order_id"].nunique())
col3.metric("Total Customers", df["customer_id"].nunique())

# Revenue by Category
st.subheader("Revenue by Category")
cat_rev = df.groupby("category")["revenue"].sum()
st.bar_chart(cat_rev)

# Top Products
st.subheader("Top Selling Products")
top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)
st.bar_chart(top_products)

# Revenue by Region
st.subheader("Revenue by Region")
region_rev = df.groupby("region")["revenue"].sum()
st.write(region_rev)
