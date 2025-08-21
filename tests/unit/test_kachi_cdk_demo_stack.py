import aws_cdk as core
import aws_cdk.assertions as assertions

from kachi_cdk_demo.kachi_cdk_demo_stack import KachiCdkDemoStack

# example tests. To run these tests, uncomment this file along with the example
# resource in kachi_cdk_demo/kachi_cdk_demo_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = KachiCdkDemoStack(app, "kachi-cdk-demo")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
