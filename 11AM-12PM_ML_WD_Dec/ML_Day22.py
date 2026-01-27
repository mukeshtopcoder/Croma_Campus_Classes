"""
Streamlit Code
"""
import streamlit as st

st.title("My Streamlit Web App")
st.write("My First Application")
st.header("Computer")
st.subheader("Analog")
st.text("Digital")
st.markdown("### Hybrid")

import pandas
data = {
'Months':['Jan','Feb','Mar','Apr','May','Jun'],
'Sales':[34567,89655,24566,76654,46755,78554]
    }
df = pandas.DataFrame(data)
st.dataframe(df)
st.button("Click Here!")
if st.button("Show Output"):
    st.write("Here is your output")

name = st.text_input("Enter Your Name : ")
if st.button("Submit"):
    st.write("Hello,",name)

age = st.number_input("Enter Age : ",min_value=0,max_value=100)
if st.button("Submit Age"):
    st.write("Age :",age)

age = st.slider("Select Age ",0,100)

col1 , col2 = st.columns(2)
with col1:
    st.text_input("Enter First Name")
with col2:
    st.text_input("Enter Last Name")

with st.container():
    st.header("Container")
    st.text("About Container")

st.sidebar.selectbox("Select",["Home",'About','Blogs'])
st.selectbox("Select",["Home",'About','Blogs'])
st.multiselect("Select",["Home",'About','Blogs'])

st.date_input("Select Date")
st.line_chart(df['Sales'])
st.bar_chart(df['Sales'])
