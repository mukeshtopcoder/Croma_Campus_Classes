import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# load dataset
df = sns.load_dataset('penguins')

# drop null values
df = df.dropna()

# data distribution
X = df[['bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g']]
y = df['species']

# data split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=11)

# model building
model = RandomForestClassifier()

# model training
model.fit(X_train,y_train)

# Save Model
pickle.dump(model , open('model/model.pkl' , 'wb')) 