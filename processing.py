# Standard Library Imports
import os
from statistics import mean, stdev

# Third Party Imports

# Local Application Imports
from functions.aws_functions import download_from_aws, get_bucket_contents
from functions.graphing import simple_graphing, total_graphing, cropped_graphing
# %% plot inline figure
from functions.cleaning_functions import clean_demand, clean_price

def download_prices():

    bucket = {'prices':'lukaprices'}

    directory = os.getcwd()
    for folder, bucket_name in bucket.items():
        bucket_contents = get_bucket_contents(bucket_name)
        filtered_bucket = [x for x in bucket_contents if not x.startswith('Archive')]
        file_list = os.listdir(directory+'/files/'+folder+'/')
        for aws_filename in filtered_bucket:
            if aws_filename not in file_list:
                download_from_aws(bucket_name, aws_filename,
                                  directory+'/files/'+folder+'/'+aws_filename)
            else:
                pass

def download_demand():

    bucket = {'demand':'fridgedemand'}

    directory = os.getcwd()
    for folder, bucket_name in bucket.items():
        bucket_contents = get_bucket_contents(bucket_name)
        filtered_bucket = [x for x in bucket_contents if not x.startswith('Archive')]
        file_list = os.listdir(directory+'/files/'+folder+'/')
        for aws_filename in filtered_bucket:
            if aws_filename not in file_list:
                download_from_aws(bucket_name, aws_filename,
                                  directory+'/files/'+folder+'/'+aws_filename)
            else:
                pass

download_prices()
download_demand()

content = ['2019-12-20_demand.csv', '2019-12-21_demand.csv', '2019-12-22_demand.csv', '2019-12-23_demand.csv', '2019-12-27_demand.csv', '2019-12-28_demand.csv', 'Archive/', 'Archive/2019-08-27_demand.csv', 'Archive/2019-08-28_demand.csv', 'Archive/2019-08-29_demand.csv', 'Archive/2019-09-01_demand.csv', 'Archive/2019-09-02_demand.csv', 'Archive/2019-09-03_demand.csv', 'Archive/2019-09-04_demand.csv', 'Archive/2019-09-05_demand.csv', 'Archive/2019-09-06_demand.csv', 'Archive/2019-09-07_demand.csv', 'Archive/2019-09-08_demand.csv', 'Archive/2019-09-09_demand.csv', 'Archive/2019-09-10_demand.csv', 'Archive/2019-09-11_demand.csv', 'Archive/2019-09-12_demand.csv', 'Archive/2019-09-13_demand.csv', 'Archive/2019-09-20_demand.csv', 'Archive/2019-09-21_demand.csv', 'Archive/2019-09-22_demand.csv', 'Archive/2019-09-23_demand.csv', 'Archive/2019-09-24_demand.csv', 'Archive/2019-09-25_demand.csv', 'Archive/2019-12-16_demand.csv', 'Archive/2019-12-18_demand.csv']




directory = os.getcwd()

demand_path = directory+'/files/demand/'
demand_df = clean_demand(demand_path)

price_path = directory+'/files/prices/'
price_df = clean_price(price_path)

# %% display a dataframe
price_df

simple_graphing(price_df)
simple_graphing(demand_df)
