"""
Script to monitor an EC2 instance.
"""
import boto3


from constans import INSTANCE_ID


def monitor_instance_status(instance_id):
    """Monitor the status of an EC2 instance."""
    ec2 = boto3.client('ec2')
    try:
        response = ec2.describe_instance_status(InstanceIds=[instance_id])
        for instance in response['InstanceStatuses']:
            instance_state = instance['InstanceState']['Name']
            system_status = instance['SystemStatus']['Status']
            instance_status = instance['InstanceStatus']['Status']
            print(
                f"Instance ID: {instance['InstanceId']},"
                f" State: {instance_state}, "
                f"System Status: {system_status}, "
                f"Instance Status: {instance_status}")
    except Exception as e:
        print(f'Error monitoring instance status: {e}')


if __name__ == '__main__':
    monitor_instance_status(INSTANCE_ID)
