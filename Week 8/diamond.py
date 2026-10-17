import pandas as pd
import matplotlib.pyplot as plt

# Dataset load
df = pd.read_csv("machine learning/diamonds.csv")

print(df)

# X = Input / Feature
X = df[["carat"]]

# y = Target
y = df["price"]


# -----------------------------------------
# Scatter Plot
# -----------------------------------------

df.plot.scatter(
    x="carat",
    y="price",
    title="Scatter Plot of Diamonds"
)

plt.show()


# -----------------------------------------
# Train Test Split
# -----------------------------------------

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X Train:")
print(X_train)

print("X Test:")
print(X_test)

print("Y Train:")
print(y_train)

print("Y Test:")
print(y_test)


# -----------------------------------------
# Linear Regression
# -----------------------------------------

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()


# -----------------------------------------
# Cross Validation
# -----------------------------------------

from sklearn.model_selection import cross_val_score, KFold

cv = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    regressor,
    X_train,
    y_train,
    cv=cv,
    scoring="neg_mean_absolute_error"
)

print("\nCross Validation Scores:")

print(-scores)

print(
    "Average Cross Validation MAE:",
    -scores.mean()
)


# -----------------------------------------
# Final Model Training
# -----------------------------------------

regressor.fit(X_train, y_train)


# Prediction
y_pred = regressor.predict(X_test)


# -----------------------------------------
# MAE
# -----------------------------------------

from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(
    y_test,
    y_pred
)

print(
    "\nFinal Test MAE:",
    mae
)


# -----------------------------------------
# R2 Score
# -----------------------------------------

from sklearn.metrics import r2_score

r2 = r2_score(
    y_test,
    y_pred
)

print(
    "R2 Score:",
    r2
)


input("Wait for me...")