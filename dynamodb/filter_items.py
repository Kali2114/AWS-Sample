"""
Script to filter items in the Music table based on genre.
"""
import boto3
from boto3.dynamodb.conditions import Attr


def filter_items_by_artist(artist):
    """Filter items in the Music table based on artist."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')

    response = table.scan(
        FilterExpression=Attr('Artist').eq(artist)
    )

    items = response.get('Items', [])
    if items:
        for item in items:
            print(f'Artist: {item['Artist']}, title: {item['Title']}')
    else:
        print(f'No items found for artist: {artist}')


if __name__ == '__main__':
    filter_items_by_artist('VNM')

