"""
Scripts for create and delete buckets with error handling.
"""
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name):
    """Create a new bucket in AWS S3."""
    s3 = boto3.client('s3')
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f'Created new bucket: {bucket_name}')
    except ClientError as e:
        print(f'Error creating bucket {bucket_name}: {e}')


def delete_bucket(bucket_name):
    """Delete bucket from AWS S3."""
    s3 = boto3.client('s3')
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f'Deleted bucket: {bucket_name}')
    except ClientError as e:
        print(f'Error deleting bucket {bucket_name}: {e}')


if __name__ == '__main__':
    create_bucket('newbucket2114')
    # delete_bucket('newbucket2114')
