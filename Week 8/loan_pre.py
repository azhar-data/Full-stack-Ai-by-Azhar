import pandas as pd
import numpy as np

df=pd.read_csv('machine learning/classification/loan preduction.csv')
print(df)

print(df.describe())
print(df.duplicated().sum())
print(df.drop_duplicates())
print(df.info())
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df['Property_Area_encoded'] = le.fit_transform(df['Property_Area'])
df['Loan_Status_encoded'] = le.fit_transform(df['Loan_Status'])


X=df[['ApplicantIncome','Credit_History','LoanAmount','Loan_Amount_Term','CoapplicantIncome']]
y=df['Loan_Status_encoded']
print(X)
print(y)




from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,
                                                 y,
                                                 train_size=.7,
                                                 random_state=25
                                                 )

print(X_test)
print(X_train)
print(y_test)
print(y_train)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))