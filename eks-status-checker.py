import boto3
import schedule

eks_client = boto3.client('eks', region_name="eu-west-3")
eks_clusters = eks_client.list_clusters().get('clusters')


def check_eks_clusters_status():
    for cluster in eks_clusters:
        response = eks_client.describe_cluster(
            name=cluster
        )
        cluster_info = response.get('cluster')
        cluster_status = cluster_info.get('status')
        cluster_endpoint = cluster_info.get('endpoint')
        cluster_version = cluster_info.get('version')

        print(f"Cluster {cluster} status is {cluster_status}")
        print(f"Cluster endpoint: {cluster_endpoint}")
        print(f"Cluster version: {cluster_version}")


schedule.every(5).hours.do(check_eks_clusters_status)

while True:
    schedule.run_pending()

