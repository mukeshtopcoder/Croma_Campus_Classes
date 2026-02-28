#   !pip install streamlit

import streamlit as st

st.title("My First Streamlit Application")
st.write("Welcome to my page")
st.text("Hello World")
st.header("Computer:")
st.subheader("Digital Computer")
st.markdown("**HELLO INDIA**")
name = st.text_input("Enter Your Name")
if name:
    st.success(f"Welcome {name}")
num = st.number_input("Enter Your Age")
course = st.selectbox("Select Course",["Python","DS",'DA'])
import pandas as pd
data = {
'empid':[101,102,103,104],
'empname':['Ram','Shyam','Mohan','Sohan'],
'empsalary':[23752,95869,47859,24968]
    }
df  = pd.DataFrame(data)
st.dataframe(df)
st.line_chart(df['empsalary'])

st.sidebar.title("Menu")
option = st.sidebar.radio("Go To",['Home','About'])
if option == 'About':
    st.title("About My Page")
