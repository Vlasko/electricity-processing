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

# Try ARIMA instead
series = demand_df['2020-01-01 00':'2020-03-20 23'].loc[:,'Demand (W)']

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(series).set_xlim([1, 11])
plt.show()

from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

# fit model
model = ARIMA(series, order=(4,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# plot residual errors
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
plt.show()
residuals.plot(kind='kde')
plt.show()
print(residuals.describe())

X = series.values[:1000] #start with first 1000 values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(4,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

# plot
plt.figure(figsize=(12,8))
plt.plot(test, label='Test Data')
plt.plot(predictions, color='red', label='Predicted Data')
plt.xlabel('Lags', fontsize=15)
plt.xlim(0,300)
plt.ylabel('Demand (W)', fontsize=15)
plt.ylim(0,250)
plt.title('Figure showing ARIMA model of fridge demand data', fontsize=18)
plt.legend()
plt.show()

# This not actually too bad, the general shape is right.
