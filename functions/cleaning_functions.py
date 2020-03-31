# Standard Library Imports
import os

# Third Party Imports
import pandas as pd

# Local Application Imports


def clean_demand(demand_path):
    demand_data = pd.DataFrame()
    for filename in os.listdir(demand_path):
        if filename.endswith('.csv'):
            with open(demand_path+filename) as f:
                data = pd.read_csv(demand_path+filename,
                                   index_col='Timestamp',
                                   parse_dates=True)
                demand_data = demand_data.append(data)
    demand_data.index = pd.to_datetime(demand_data.index)
    demand_data.sort_index()
    resampled_demand = demand_data.resample('15T').mean()

    return resampled_demand



def clean_price(price_path):
    price_data = pd.DataFrame()
    for filename in os.listdir(price_path):
        if filename.endswith('.csv'):
            with open(price_path+filename) as f:
                data = pd.read_csv(price_path+filename,
                                   index_col='Timestamp',
                                   parse_dates=True)
                price_data = price_data.append(data)
    price_data.index = pd.to_datetime(price_data.index.tz_localize('UTC'))
    price_data = price_data.shift(1,'H') # temporary fix for time zone issue
    price_data = price_data.loc[~price_data.index.duplicated(keep='first')]
    resampled_price = price_data.resample('15T').ffill()

    return resampled_price
