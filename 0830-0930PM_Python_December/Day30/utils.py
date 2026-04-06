import pandas as pd

def load_data(file):
    df = pd.read_csv(file)
    df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
    return df

def clean_data(df):
    df = df.dropna()
    return df

def filter_data(df , region , category):
    if region != "All":
        df = df[df['Region']==region]
    if category != "All":
        df = df[df['Product_Category']==category]
    return df 