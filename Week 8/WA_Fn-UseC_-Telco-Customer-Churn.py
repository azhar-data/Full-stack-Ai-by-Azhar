import pandas as pd 
import numpy as np 

df=pd.read_csv('machine learning/classification/WA_Fn-UseC_-Telco-Customer-Churn.csv')
print(df)

print('decribe of the file:',df.describe())
print(df.dtypes)
print(df.info())
print(df.drop)
print(df.drop_duplicates())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

df['Partner_encoded'] = le.fit_transform(df['Partner'])
df['InternetService_encoded'] = le.fit_transform(df['InternetService'])
df['Contract_encoded'] = le.fit_transform(df['Contract'])
df['PaymentMethod_encoded'] = le.fit_transform(df['PaymentMethod'])
df['PaperlessBilling_encoded'] = le.fit_transform(df['PaperlessBilling'])

X=df[['tenure','InternetService_encoded','PaymentMethod_encoded','Contract_encoded']]
y = le.fit_transform(df['Churn'])
print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,
                                                y,
                                                train_size=.8,
                                             random_state=25
                                             )

print(X_test)
print(X_train)
print(y_test)
print(y_train)

from sklearn.ensemble import RandomForestClassifier
logreg=RandomForestClassifier()
logreg.fit(X_train,y_train)


y_pred = logreg.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))
