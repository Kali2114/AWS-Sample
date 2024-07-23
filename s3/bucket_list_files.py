"""Script to list files in bucket."""
import boto3


def list_files_in_bucket(bucket_name):
    """List all files inside S3 AWS bucket."""
    s3 = boto3.client('s3')
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print(f'Bucket {bucket_name} is empty.')


list_files_in_bucket('buckethat2114')
