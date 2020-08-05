# Standard Library Imports
import os
import pandas as pd
import numpy as np

# Third Party Imports
from functions.cleaning_functions import clean_demand
import matplotlib.pyplot as plt
import seaborn as sns

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

data = demand_df['2020-01-01 00':'2020-03-20 23']
data.loc[:,'Time'] = data.index.time
data

# Histogram
data.hist()

# Heatmap
corr = data.corr()
f, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(corr,annot=True, cmap="coolwarm")

#Sklearn Libraries

# Import train_test_split to split the data into training and testing set
from sklearn.model_selection import train_test_split

#Import the model (Linear Regression)
from sklearn.linear_model import LinearRegression   # linear regression model

#Import metrics to evaluate the model
from sklearn.metrics import mean_squared_error, mean_absolute_error
