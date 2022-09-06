from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    assertions
)

from tutorial.hitcounter import HitCounter


def test_dynamo_db_table_created():
    stack = Stack()
    hitcounter = HitCounter(
        stack, "HitCounterTest",
        downstream=_lambda.Function(stack,
                                    "FakeFunction",
                                    code=_lambda.Code.from_asset("lambda"),
                                    handler="lala.handler",
                                    runtime=_lambda.Runtime.PYTHON_3_7)
    )

    template = assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::DynamoDB::Table", count=1)
