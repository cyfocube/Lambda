import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    response = ec2.describe_instances()
    
   
    instance_counts = sum(len(reservation['Instances']) for reservation in response['Reservations'])
    
    return {
        'statusCode': 200,
        'body': {
            'instanceCount': instance_count
        }
    }
