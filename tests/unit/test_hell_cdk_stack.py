import aws_cdk as core
import aws_cdk.assertions as assertions

from hell_cdk.hell_cdk_stack import hellcdkstack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_project/cdk_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = hellcdkstack(app, "hell_cdk")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
