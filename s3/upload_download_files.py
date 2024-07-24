"""
Scripts to upload and download files from buckets.
"""
import boto3
from botocore.exceptions import ClientError


def upload_file(bucket_name, file_path, key):
    """Upload file to an S3 bucket."""
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_path, bucket_name, key)
        print(f'File {file_path} uploaded to {bucket_name} with key {key}')
    except ClientError as e:
        print(f'Error uploading file {file_path} to bucket {bucket_name}: {e}')

def download_file(bucket_name, key, download_path):
    """Download file from S3 bucket."""
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket_name, key, download_path)
        print(f'File {key} downloaded from {bucket_name} to {download_path}')
    except ClientError as e:
        print(f'Error downloading file {key} from bucket {bucket_name}: {e}')


# file_path_upload = '/home/kamileg/PycharmProjects/AWS-Sample/sample.txt'
# upload_file('buckethat2114', file_path_upload, 'new_file.txt')

file_path_download = '/home/kamileg/PycharmProjects/AWS-Sample/download.txt'
download_file('buckethat2114', 'new_file.txt', file_path_download)
