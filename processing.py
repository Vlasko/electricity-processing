# Standard Library Imports
import os
import pandas as pd
# from statistics import mean, stdev

# Third Party Imports
from functions.graphing import simple_graphing #, total_graphing, cropped_graphing
# %% plot inline figure
from functions.cleaning_functions import clean_demand, clean_price
from functions.download_functions import download_prices, download_demand

download_prices()
download_demand()

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

price_path = directory+'/files/prices/'
price_df = clean_price(price_path)

# %% display a dataframe
merged_df = pd.merge(demand_df, price_df, left_index = True, right_index = True)

simple_graphing(price_df['2019-12-28':])
simple_graphing(demand_df['2019-12-28':])
