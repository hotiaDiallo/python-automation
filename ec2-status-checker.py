import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="eu-west-3")


def check_instance_status():
    ec2_statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
    )
    for status in ec2_statuses.get('InstanceStatuses'):
        ins_status = status.get('InstanceStatus').get('Status')
        sys_status = status.get('SystemStatus').get('Status')
        state = status.get('InstanceState').get('Name')
        print(f"Instance {status['InstanceId']} is {state} with instance status {ins_status} and system status {sys_status}")
    print("#############################\n")


schedule.every(5).seconds.do(check_instance_status)

while True:
    schedule.run_pending()
