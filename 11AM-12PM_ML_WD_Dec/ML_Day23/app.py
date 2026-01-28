import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model    import LogisticRegression
from sklearn.metrics         import accuracy_score

df = pd.read_csv("diabetes.csv")
df = df.dropna()
df = df.drop_duplicates()


X = df.drop(columns=["Outcome"])
y = df['Outcome']

X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=11,test_size=0.20)
model = LogisticRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_pred,y_test)

st.subheader("User Inputs")

def user_input():
    Pregnancies = st.slider("Pregnancies",0,17,1)
    Glucose = st.slider("Glucose",0,200,120)
    BloodPressure = st.slider("BloodPressure",0,122,80)
    SkinThickness = st.slider("SkinThickness",0,99,34)
    Insulin = st.slider("Insulin",0,846,340)
    BMI = st.slider("BMI",0.00,70.00,45.00)
    DiabetesPedigreeFunction = st.slider("DiabetesPedigreeFunction",0.001,2.500,0.456)
    Age = st.slider("Age",18,90,28)
    return np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

inputs = user_input()
if st.button("Submit"):
    pred = model.predict(inputs)
    if pred[0]==1:
        st.error("Diabetes")
    else:
        st.success("No Diabetes")
