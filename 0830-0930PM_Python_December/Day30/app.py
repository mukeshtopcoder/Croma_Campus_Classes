import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import load_data , clean_data , filter_data
import streamlit as st  

st.set_page_config( page_title="Sales Dashboard" , layout='wide' )

st.title("Sales Data Analysis Dashboard")

# Load Dataset
df = load_data('dataset/sales_data.csv')

# Data Cleaning (Remove Null Values)
df = clean_data(df)

# Sidebar Filters
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region",["All"]+list(df['Region'].unique()))
category = st.sidebar.selectbox("Select Product Category",["All"]+list(df['Product_Category'].unique()))

filtered_df = filter_data(df,region,category)

st.dataframe(filtered_df.head())
