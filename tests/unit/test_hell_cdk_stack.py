import aws_cdk as core
import aws_cdk.assertions as assertions

from hell_cdk.hell_cdk_stack import HellCdkStack

# example tests. To run these tests, uncomment this file along with the example
# resource in hell_cdk/hell_cdk_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = HellCdkStack(app, "hell-cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
