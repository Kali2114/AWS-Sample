"""
Script to create table in dynamodb.
"""
import boto3


def create_table():
    """Create a table in DynamoDB with specified schema."""
    dynamodb = boto3.resource('dynamodb')
    try:
        table = dynamodb.create_table(
            TableName='Music',
            KeySchema=[
                {
                    'AttributeName': 'Artist',
                    'KeyType': 'HASH',
                },
                {
                    'AttributeName': 'Title',
                    'KeyType': 'RANGE',
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Artist',
                    'AttributeType': 'S',
                },
                {
                    'AttributeName': 'Title',
                    'AttributeType': 'S',
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10,
            }
        )
        table.meta.client.get_waiter('table_exists').wait(TableName='Music')
        print(f"Table {table.table_name} created successfully.")
    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    create_table()