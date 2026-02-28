import numpy as np
import pandas as pd
import streamlit as st

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title='My ML App',layout='centered')
st.title("Iris Flower Application")

data = load_iris()
X = data.data
y = data.target

feature_names = data.feature_names
target_names = data.target_names

model = RandomForestClassifier()
model.fit(X,y)


st.subheader('Enter Flower Measurements : ')
# User Inputs
sepal_length = st.slider("Sepal Length (cm)",4.0,8.0,5.4)
sepal_width = st.slider("Sepal Width (cm)",2.0,5.0,3.4)
petal_length = st.slider("Petal Length (cm)",1.0,8.0,1.3)
petal_width = st.slider("Petal Width (cm)",1.0,2.5,1.6)
myinput = [[sepal_length,sepal_width,petal_length,petal_width]]
# Prediction
if st.button("Predict"):
    predict = model.predict(myinput)
    predicted_class = target_names[predict][0]
    st.success(f"Predicted Flower : {predicted_class}")

# Show Dataset
if st.checkbox("Show Dataset"):
    df = pd.DataFrame(X , columns=feature_names)
    df['species'] = y
    st.dataframe(df)
