from aws_cdk import (
    Duration,
    Stack, # is a base class that represents a CloudFormation stack. By inheriting from it, your class automatically becomes a CDK stack and can define AWS resources
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
)
from constructs import Construct

class KachiCdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # 1️⃣ Create a VPC
        vpc = ec2.Vpc(
            self, "DemoEksVpc",
            vpc_name="Vpc-demo",
            max_azs=2  # Use 2 Availability Zones for HA
        )

        # 2️⃣ IAM Role for Cluster Admin
        cluster_admin = iam.Role(
            self, "DemoClusterAdminRole",
            role_name="cluster-roles",
            assumed_by=iam.AccountRootPrincipal()
        )

        # 3️⃣ Create EKS Cluster
        cluster = eks.Cluster(
            self, "DemoEksCluster",
            cluster_name="demo-cluster",
            version=eks.KubernetesVersion.V1_29,
            vpc=vpc,
            default_capacity=0,  # We'll use managed nodegroup instead
            masters_role=cluster_admin
        )

        # 4️⃣ Add Managed Node Group
        cluster.add_nodegroup_capacity(
            "DemoNodeGroup",
            nodegroup_name="demo-cluster-node-group",
            desired_size=1,
            min_size=1,
            max_size=3,
            instance_types=[ec2.InstanceType("t3.small")]
        )
