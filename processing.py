# Standard Library Imports
import os
from statistics import mean, stdev

# Third Party Imports

# Local Application Imports
from functions.AWS_functions import download_from_aws, get_bucket_contents
from functions.graphing import simple_graphing, total_graphing, cropped_graphing
# %% plot inline figure
from functions.cleaning_functions import clean_demand, clean_price

buckets = {'Prices':'lukaprices',
           'Demand':'fridgedemand',
           'Temperature':'fridgetemperature'}

directory = os.getcwd()
for folder, bucket_name in buckets.items():
    bucket_contents = get_bucket_contents(bucket_name)
    file_list = os.listdir(directory+'files/'+folder+'/')
    for aws_filename in bucket_contents:
        if aws_filename not in file_list:
            download_from_aws(bucket_name, aws_filename,
                              directory+'files/'+folder+'/'+aws_filename)
        else:
            pass

directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

price_path = directory+'/files/prices/'
price_df = clean_price(price_path)

# %% display a dataframe
price_df

simple_graphing(price_df)
