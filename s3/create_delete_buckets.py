"""
Scripts for create and delete buckets.
"""
import boto3


def create_bucket(bucket_name):
    """Create a new bucket in AWS S3."""
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    print(f'Create new bucket: {bucket_name}')


def delete_bucket(bucket_name):
    """Delete bucket from AWS S3."""
    s3 = boto3.client('s3')
    s3.delete_bucket(Bucket=bucket_name)
    print(f'Delete bucket {bucket_name}')


create_bucket('newbucket2114')
# delete_bucket('newbucket2114')
