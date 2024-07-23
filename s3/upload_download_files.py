"""
Scripts to upload and download files from buckets.
"""
import boto3


def upload_file(bucket_name, file_path, key):
    """Upload file to an S3 bucket."""
    s3 = boto3.client('s3')
    s3.upload_file(file_path, bucket_name, key)
    print(f'File {file_path} uploaded to {bucket_name} with key {key}')


def download_file(bucket_name, key, download_path):
    """Download file from S3 bucket."""
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, key, download_path)
    print(f"File {key} downloaded from {bucket_name} to {download_path}")


# file_path_upload = '/home/kamileg/PycharmProjects/AWS-Sample/sample.txt'
# upload_file('buckethat2114', file_path_upload, 'new_file.txt')

file_path_download = '/home/kamileg/PycharmProjects/AWS-Sample/download.txt'
download_file('buckethat2114', 'new_file.txt', file_path_download)
