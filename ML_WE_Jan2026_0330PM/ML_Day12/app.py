import streamlit as st
import pickle

model = pickle.load(open("model/model.pkl","rb"))

st.title("Penguin Predictive Model")

st.write("Enter Penguins Details")

bill_lenght = st.number_input('bill_length_mm')
bill_depth = st.number_input('bill_depth_mm')
flipper_lenght = st.number_input('flipper_length_mm')
body_mass = st.number_input('body_mass_g')

if st.button("Predict"):
    pred = model.predict([[bill_lenght,bill_depth,flipper_lenght,body_mass]])
    st.success(f"Predicted Penguine : {pred[0]}")
