import boto3
from datetime import datetime, timedelta, timezone

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')
    instances = ec2_client.describe_instances()['Reservations']
    
 
    current_time = datetime.now(timezone.utc)
    

    two_minutes_ago = current_time - timedelta(minutes=2)
    
    for reservation in instances:
        for instance in reservation['Instances']:
   
            launch_time = instance['LaunchTime']

            if launch_time > two_minutes_ago:
                instance_id = instance['InstanceId']
                ec2_client.terminate_instances(InstanceIds=[instance_id])
                print(f"Terminated instance {instance_id}")
