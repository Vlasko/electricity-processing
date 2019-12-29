# Standard Library Imports
import os

# Local Application Imports
from functions.aws_functions import download_from_aws, get_bucket_contents

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
