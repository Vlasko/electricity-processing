# Device Manager
import os

from functions.AWS_functions import download_from_aws, get_bucket_contents

buckets = {'Prices':'lukaprices',
           'Demand':'fridgedemand',
           'Temperature':'fridgetemperature'}

directory = os.path.split(os.getcwd())[0]
for folder, bucket_name in buckets.items():
    bucket_contents = get_bucket_contents(bucket_name)
    file_list = os.listdir(directory+'files/'+folder+'/')
    for aws_filename in bucket_contents:
        if aws_filename not in file_list:
            download_from_aws(bucket_name, aws_filename,
                              directory+'files/'+folder+'/'+aws_filename)
        else:
            pass
