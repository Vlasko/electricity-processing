# Standard Library Imports
import os
import pandas as pd

# Third Party Imports
from functions.cleaning_functions import clean_demand, clean_price
from functions.graphing import simple_graphing, combined_graphing #, total_graphing, cropped_graphing

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

price_path = directory+'/files/prices/'
price_df = clean_price(price_path)

# %% display a dataframe
merged_df = pd.merge(demand_df, price_df, left_index = True, right_index = True)

combined_graphing(price_df['2020-01-01':],demand_df['2020-01-01':])
simple_graphing(price_df['2019-12-28':])
simple_graphing(demand_df['2019-12-28':])

mask = price_df.loc[:,'Electricity Price(p/kWh)']<1
price_df[mask]
