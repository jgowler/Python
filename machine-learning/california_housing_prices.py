######################################################
# Predict California Housing prices based on dataset #
######################################################

# Import the dataset:
from sklearn.datasets import fetch_california_housing
# Import the models package:
from sklearn.neighbors import KNeighborsRegressor
# Import Scaler:
from sklearn.preprocessing import StandardScaler
# Import Pipelin to chain processing steps:
from sklearn.pipeline import Pipeline
# Import Gridsearch:
from sklearn.model_selection import GridSearchCV
# Import PyPlot:
import matplotlib.pylab as plt
# Import Pandas:
import pandas as pd

# Get data from dataset:
x, y = fetch_california_housing(return_X_y=True)
# Assign models package to variable:
mod = KNeighborsRegressor()
# Train the model on parameters passed to it:
mod.fit(x, y)
# Start a Pipline object(list of tuples):
pipe = Pipeline ([
    ("scale", StandardScaler()),
    ("model", KNeighborsRegressor(n_neighbors=1))
])
# Ste up cross validation
mod = GridSearchCV(estimator=pipe,
             param_grid={'model__n_neighbors': [1,2,3,4,5,6,7,8,9]},
             cv=3)
# Train and fit the pipeline on the data with scaling:
mod.fit(x, y)
mod.cv_results_
# Get predictions based on the data of the dataset:
predictions = mod.predict(x)
# Put the predictions on the X axis, and predicted values on the Y axis:
