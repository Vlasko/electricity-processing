# Standard Library Imports
import os
import pandas as pd
import numpy as np

# Third Party Imports
from functions.cleaning_functions import clean_demand
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)
demand_df.dropna(inplace=True)

data = demand_df['2020-01-01 00':'2020-03-20 23']
data.loc[:,'Time'] = data.index.time
data

## Histogram
# data.hist()

# Heatmap
corr = data.corr()
f, ax = plt.subplots(figsize=(12, 10))
# sns.heatmap(corr,annot=True, cmap="coolwarm")

#Sklearn Libraries



data.isnull().values.any()


SEED = 1234
timestamps = data.index.astype(np.int64).to_numpy().reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(timestamps, data.loc[:,'Demand (W)'],
                                                    test_size=0.2,
                                                    random_state=SEED)

model = LinearRegression()
model.fit(X_train, y_train)

y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

RMSE_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
RMSE_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
print(RMSE_train, RMSE_test)

R_squared = model.score(X_test, y_test)
print(R_squared)

# Ideal scenario
plt.plot(y_train,y_train,c='r',label='If Perfectly Predicted')

# Reality
plt.scatter(y_train_pred, y_train, marker='o')

plt.xlabel('Predicted y')
plt.ylabel('Actual y')
plt.legend(loc="best")
plt.show()


# Linear regression does not work here, all predicted values are around 27 W,
# when in fact the demand from the fridge is often around zero, but then spikes
# to values of around 100 W.
