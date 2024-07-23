"""
CRUD for datafiles.
"""
import boto3


def add_item(artist, title):
    """Add an item to the Music table."""

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')

    response = table.put_item(
        Item={
            'Artist': artist,
            'Title': title,
        }
    )
    print(f'Added item: {artist} - {title}')
    return response


def get_item(artist, title):
    """Retrieve an item from the Music table."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')

    response = table.get_item(
        Key={
            'Artist': artist,
            'Title': title,
        }
    )
    item = response.get('Item')

    if item:
        print(f'Retrieved data: {item}')
    else:
        print(f'Item not found.')
    return item


def delete_item(artist, title):
    """Delete an item from the Music table."""
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Music')

    item = get_item(artist, title)
    if not item:
        print("Item with artist {artist} and title {title} not found.")
        return

    response = table.delete_item(
        Key={
            'Artist': artist,
            'Title': title,
        }
    )
    print(f"Deleted item: {artist} - {title}")
    return response


def update_title(artist, old_title, new_title):
    """Update the title of an item in the Music table."""
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('Music')

    # Retrieve the current item
    item = get_item(artist, old_title)
    if not item:
        print(f'Item with artist {artist} and title {old_title} not found')
        return

    item['Title'] = new_title
    table.put_item(Item=item)

    delete_item(artist, old_title)

    print(f'Updated item: {artist} - {old_title} to new title: {new_title}')


if __name__ == '__main__':
    # add_item('VNM', 'EDKT')
    # get_item('VNM', 'EDKT')
    # delete_item('VNM', 'EDKT')
    update_title('VNM', 'EDKT', 'PROPEJN')