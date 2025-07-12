from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("datasets/bmw.csv")

x = pd.get_dummies(df.drop("price", axis=1))
y = df["price"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

pipe = Pipeline([
    ("model", RandomForestRegressor())
])

param_grid = {
    'model__n_estimators': [50, 100],
    'model__max_depth': [None, 10, 20]
}

mod = GridSearchCV(estimator=pipe, param_grid=param_grid, cv=5)

mod.fit(X_train, y_train)

pred = mod.predict(X_test)

plt.scatter(pred, y_test)
plt.xlabel("Predicted Price")
plt.ylabel("Actual Price")
plt.title("Predicted vs Actual Car Prices")
plt.show()
