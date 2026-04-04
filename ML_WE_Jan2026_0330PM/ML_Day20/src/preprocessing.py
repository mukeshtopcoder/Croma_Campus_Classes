# Importing Libraries
from sklearn.preprocessing import LabelEncoder, StandardScaler

def preprocessing_data(df):
    # Removing Null Values
    df = df.dropna()

    # Removing Columns (Feature Engineering)
    df = df.drop(columns=['RowNumber', 'CustomerId', 'Surname'])

    # Scaling and Encoding
    le = LabelEncoder()
    scaler = StandardScaler()
    # Encoding
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col]) 
    # Data Division
    X = df.drop(columns=['Exited'])
    y = df['Exited']
    # Scaling
    X = scaler.fit_transform(X)
    return X,y
