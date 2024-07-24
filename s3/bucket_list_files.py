"""
Script to list files in bucket with error handling.
"""
import boto3
from botocore.exceptions import ClientError

def list_files_in_bucket(bucket_name):
    """List all files inside S3 AWS bucket."""
    s3 = boto3.client('s3')
    try:
        response = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print(f'Bucket {bucket_name} is empty.')
    except ClientError as e:
        print(f'Error listing files in bucket {bucket_name}: {e}')


list_files_in_bucket('buckethat2114')
