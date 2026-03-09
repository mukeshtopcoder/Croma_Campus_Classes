import pandas as pd
import seaborn as sns
df = sns.load_dataset("tips")

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

X = df[['total_bill', 'sex', 'smoker', 'day', 'time', 'size']]
y = df['tip']

X.sex = X.sex.map(lambda x: 1 if x == 'Male' else 0 )
X.smoker = X.smoker.map(lambda x: 1 if x == 'Yes' else 0 )
X.day = X.day.map(lambda x: list(X.day.unique()).index(x))
X.time = X.time.map(lambda x: 0 if x == 'Lunch' else 1)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
model = LinearRegression()

model.fit(X_train, y_train)
pickle.dump(model, open("model/model.pkl", "wb"))