import boto3

ec2_client = boto3.client('ec2', region_name="eu-west-3")
ec2_resource = boto3.resource('ec2', region_name="eu-west-3")

ec2_virginia_client = boto3.client('ec2', region_name="us-east-1")
ec2_virginia_resource = boto3.resource('ec2', region_name="us-east-1")

reservations_in_paris = ec2_client.describe_instances()['Reservations']
instance_ids_in_paris = []

for res in reservations_in_paris:
    instances = res['Instances']
    for instance in instances:
        instance_ids_in_paris.append(instance['InstanceId'])

response = ec2_resource.create_tags(
    Resources=instance_ids_in_paris,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'PROD'
        },
    ]
)

reservations_in_virginia = ec2_virginia_client.describe_instances()['Reservations']
instance_ids_in_virginia = []

for res in reservations_in_virginia:
    instances = res['Instances']
    for ins in instances:
        instance_ids_in_virginia.append(ins['InstanceId'])

response = ec2_virginia_resource.create_tags(
    Resources=instance_ids_in_virginia,
    Tags=[
        {
            'Key': 'environment',
            'Value': 'DEV'
        },
    ]
)