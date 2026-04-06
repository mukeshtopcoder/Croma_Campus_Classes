import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split    

from src.model import train_model
from src.preprocessing import preprocessing_data
from src.utilis import evaluate_model

st.set_page_config(page_title="Churn Prediction Model" , layout='wide')

st.title("Customer Churn Prediction Model Using SVM")

st.sidebar.header("Model Settings")

uploaded_file = st.sidebar.file_uploader("Upload Your Datatset",type=['csv'])

C = st.sidebar.slider("C (Regularization)",0.1,10.0,1.0)
kernel = st.sidebar.selectbox("Kernel",['linear','rbf','poly'])
test_size = st.sidebar.slider("Test Size",0.1 , 0.5 , 0.2)

# Main Application
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df.CreditScore = df.CreditScore.astype(float)
    st.subheader("Dataset Preview")
    st.dataframe(df.head() , use_container_width=True)
    X,y = preprocessing_data(df)
    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=test_size , random_state=42)
    model = train_model(X_train,y_train,C,kernel)
    y_pred = model.predict(X_test)
    acc,cr,cm = evaluate_model(y_pred,y_test)
    col1,col2 = st.columns(2)
    with col1:
        st.subheader("Accuracy Score")
        st.metric(label="Accuracy Score", value=acc*100)
        st.subheader("Classification Report")
        st.text(cr)
    with col2:
        st.subheader("Confusion Matrix")
        fig, ax = plt.subplots()
        sns.heatmap(cm , annot=True , fmt='d' , ax=ax)
        ax.set_xlabel("Predicted Value")
        ax.set_ylabel("Actual Value")
        st.pyplot(fig)

    # Feature Distribution
    st.subheader("Feature Distribution")
    feature = st.selectbox("Select Feature",df.select_dtypes(include='float').columns)
    fig , ax = plt.subplots(figsize=(8,3))
    sns.histplot( df[feature] , ax=ax , kde=True )
    st.pyplot(fig)
    st.success("Model Trained Successfully!")
else:
    st.success("upload Your CSV File!") 