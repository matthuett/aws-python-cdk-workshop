from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_apigateway as apigw,
)
from cdk_dynamo_table_view import TableViewer
from tutorial.hitcounter import HitCounter


class TutorialStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = aws_lambda.Function(
            self,
            "HelloHandler",
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            code=aws_lambda.Code.from_asset("lambda"),
            handler="hello.handler"
        )

        lambda_with_hitcounter = HitCounter(
            self,
            "lambda_with_hitcounter",
            downstream=my_lambda,
        )

        api = apigw.LambdaRestApi(
            self,
            "Endpoint",
            handler=lambda_with_hitcounter._handler,
        )

        table_viewer = TableViewer(
            self,
            "table_viewer",
            title="Hello Hits",
            table=lambda_with_hitcounter.table,
            sort_by="-hits"

        )

