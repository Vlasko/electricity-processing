# Third Party Imports
import boto3
from botocore.exceptions import NoCredentialsError

# Local Application Imports
from keys.aws_keys import ACCESS_KEY, SECRET_KEY

def get_bucket_contents(bucket_name):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        key_list=[]
        for key in s3.list_objects(Bucket=bucket_name)['Contents']:
            key_list.append(key['Key'])
        print("Contents found")
        return key_list
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def download_from_aws(bucket_name, aws_filename, local_destination):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.download_file(bucket_name, aws_filename, local_destination)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
