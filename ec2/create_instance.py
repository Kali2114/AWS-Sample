"""
Script for create EC2 instance.
"""
import boto3

from constans import IMAGE_ID

def create_ec2_instance(image_id, instance_type, key_name):
    """Create a new EC2 instance."""
    ec2 = boto3.resource('ec2')
    try:
        instance = ec2.create_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            MinCount=1,
            MaxCount=1,
            KeyName=key_name,
        )
        instance_id = instance[0].id
        print(f'Created instance with ID: {instance_id}')
        return instance
    except Exception as e:
        print(f'Error creating instance: {e}')
        return None


if __name__ == "__main__":
    image_id = IMAGE_ID
    instance_type = 't2.micro'
    key_name = 'ec2keys'

    instance_id = create_ec2_instance(image_id, instance_type, key_name)
    