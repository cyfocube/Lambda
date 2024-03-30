import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
   
    ec2_client = boto3.client('ec2')
    

    current_time = datetime.now()
    
   
    thirty_days_ago = current_time - timedelta(days=30)
    
  
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
 
    for snapshot in snapshots:
        
        snapshot_creation_time = snapshot['StartTime']
        
    
        snapshot_creation_time = datetime.strptime(snapshot_creation_time, '%Y-%m-%dT%H:%M:%S.%fZ')
        
       
        if snapshot_creation_time > thirty_days_ago:
 
            snapshot_id = snapshot['SnapshotId']
            ec2_client.delete_snapshot(SnapshotId=snapshot_id)
            print(f"Deleted snapshot {snapshot_id}")
