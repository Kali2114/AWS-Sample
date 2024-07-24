"""
Script to display all items in the Music table.
"""
import boto3


def display_all_items():
    """Display all items in the Music table."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')

    response = table.scan()
    items = response.get('Items', [])

    if items:
        for item in items:
            print(f'Artist: {item['Artist']}, title: {item['Title']}')
    else:
        print('No items found in the Music table.')


if __name__ == '__main__':
    display_all_items()