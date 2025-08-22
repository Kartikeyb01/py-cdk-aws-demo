from aws_cdk import (
    Stack, # is a base class that represents a CloudFormation stack. By inheriting from it, your class automatically becomes a CDK stack and can define AWS resources
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
)
from constructs import Construct
from aws_cdk.lambda_layer_kubectl_v33 import KubectlV33Layer

class KachiCdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, config: dict, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC
        vpc = ec2.Vpc(
            self, "EksVpc",
            vpc_name=config["vpc_name"],
            max_azs=2
        )

        #  IAM Role
        cluster_admin = iam.Role(
            self, "ClusterAdminRole",
            role_name=f"{config['cluster_name']}-admin-role",
            assumed_by=iam.AccountRootPrincipal()
        )

        # EKS Cluster
        cluster = eks.Cluster(
            self, "EksCluster",
            cluster_name=config["cluster_name"],
            vpc=vpc,
            default_capacity=0,
            masters_role=cluster_admin,
            version=eks.KubernetesVersion.V1_33,
            kubectl_layer=KubectlV33Layer(self, "kubectl")
        )

        # Managed Node Group
        cluster.add_nodegroup_capacity(
            "NodeGroup",
            nodegroup_name=config["nodegroup_name"],
            desired_size=config["desired_size"],
            min_size=config["min_size"],
            max_size=config["max_size"],
            instance_types=[ec2.InstanceType(config["instance_type"])]
        )