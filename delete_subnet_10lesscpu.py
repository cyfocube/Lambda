# First, I will need to configure CloudWatch metric filters to capture CPU utilization 
import boto3

def lambda_handler(event, context):
 
    ec2_client = boto3.client('ec2')

    subnets = ec2_client.describe_subnets()['Subnets']
    
  
    subnets_below_10_percent = []
    
    for subnet in subnets:
        subnet_id = subnet['SubnetId']
        
    
    return subnets_below_10_percent
