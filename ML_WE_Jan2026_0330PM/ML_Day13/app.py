import streamlit as st
import pandas as pd

st.title("Tip Prediction App")
st.write("This app predicts the tip amount based on the total bill, size of the party, and other factors.")
total_bill = st.number_input("Total Bill", min_value=0.0, step=0.1)
size = st.number_input("Size of the Party", min_value=1, step=1)
sex = st.selectbox("Gender", options=["Male", "Female"])
smoker = st.selectbox("Smoker", options=["Yes", "No"])  
day = st.selectbox("Day", options=["Thur", "Fri", "Sat", "Sun"])
time = st.selectbox("Time", options=["Lunch", "Dinner"])

if st.button("Predict Tip"):
    # Load the model
    import pickle
    model = pickle.load(open("model/model.pkl", "rb"))
    
    # Prepare the input data
    input_data = pd.DataFrame({
        "total_bill": [total_bill],
        "sex": [1 if sex == "Male" else 0],
        "smoker": [1 if smoker == "Yes" else 0],
        "day": [list(["Thur", "Fri", "Sat", "Sun"]).index(day)],
        "time": [0 if time == "Lunch" else 1],
        "size": [size]
    })
    # Make the prediction
    predicted_tip = model.predict(input_data)
    st.write(f"Predicted Tip: ${predicted_tip[0]}")    
