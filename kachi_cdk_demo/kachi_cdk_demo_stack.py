from aws_cdk import (
    Duration,
    Stack, # is a base class that represents a CloudFormation stack. By inheriting from it, your class automatically becomes a CDK stack and can define AWS resources
    aws_sqs as sqs, #namespaces for AWS services
)
from constructs import Construct

class KachiCdkDemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        queue = sqs.Queue(
            self, "KachiCdkDemoQueue",
            visibility_timeout=Duration.seconds(300),
        )
