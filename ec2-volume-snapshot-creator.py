import boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-east-1")


def create_volume_snapshots():
    ec2_volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod']
            }
        ]
    )

    print(ec2_volumes)

    for volume in ec2_volumes.get('Volumes'):
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume.get('VolumeId')
        )
        print(new_snapshot)


schedule.every().day.at("06:00").do(create_volume_snapshots)

while True:
    schedule.run_pending()
