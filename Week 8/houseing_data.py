import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('machine learning/reggression/housing.csv')
print(df)
print(df.describe())
print(df.info())
print(df.dtypes)
print(df.isnull().sum())

X=df[['total_rooms','median_income','latitude','longitude','population']]
y=df['median_house_value']
print(X)
print(y)

sns.scatterplot(data=df,x='total_rooms',y='median_house_value')
plt.show()

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,
                                                y,
                                                train_size=.7,
                                                random_state=25
                                                )

print(X_train)
print(X_test)
print(y_test)
print(y_train)

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor() 
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

from sklearn.metrics import mean_absolute_error,r2_score

print('mean ..........:',mean_absolute_error(y_test,y_pred))
print('R2 score:', r2_score(y_test, y_pred))
input('wait for me....')