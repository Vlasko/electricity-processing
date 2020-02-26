# Standard Library Imports
import os
import pandas as pd

# Third Party Imports
from functions.cleaning_functions import clean_demand, clean_price
from functions.graphing_functions import simple_graphing, combined_graphing #, total_graphing, cropped_graphing

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

price_path = directory+'/files/prices/'
price_df = clean_price(price_path)

combined_df = pd.concat([demand_df, price_df], axis=1).dropna()

combined_df.loc[:,'Price (p)'] = combined_df.loc[:,'Demand (W)']*(0.25/1000)*combined_df.loc[:,'Electricity Price(p/kWh)']
combined_df.describe()
combined_df.loc[:,'Price (p)'].sum()

combined_graphing(price_df['2020-01-01':],demand_df['2020-01-01':])
simple_graphing(price_df['2020-01-01':])
simple_graphing(demand_df['2020-01-01':])

mask = combined_df.loc[:,'Electricity Price(p/kWh)']<1
combined_df[mask]
