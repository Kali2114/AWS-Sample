"""
Scripts for start, stop and terminate instance.
"""
import boto3

from constans import INSTANCE_ID


def start_instance(instance_id):
    """Start an EC2 instance."""
    ec2 = boto3.client('ec2')
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        print(f'Started instance with ID: {instance_id}')
    except Exception as e:
        print(f'Error starting instance: {e}')


def stop_instance(instance_id):
    """Stop an EC2 instance."""
    ec2 = boto3.client('ec2')
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        print(f'Stopped instance with ID: {instance_id}')
    except Exception as e:
        print(f'Error stopping instance: {e}')


def terminate_instance(instance_id):
    """Terminate an EC2 instance."""
    ec2 = boto3.client('ec2')
    try:
        ec2.terminate_instances(InstanceIds=[instance_id])
        print(f'Stopped instance with ID: {instance_id}')
    except Exception as e:
        print(f'Error stopping instance: {e}')


if __name__ == '__main__':
    start_instance(INSTANCE_ID)
    # stop_instance(INSTANCE_ID)