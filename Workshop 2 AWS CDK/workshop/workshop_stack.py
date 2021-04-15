from aws_cdk import core
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_s3 import Bucket
from aws_cdk.aws_s3_notifications import LambdaDestination


class WorkshopStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = Bucket(
            scope=self,
            id='WorkshopBucket',
            bucket_name='cloudvisor-workshop-bucket'
        )

        function = Function(
            scope=self,
            id='WorkshopFunction',
            function_name='WorkshopFunction',
            runtime=Runtime.PYTHON_3_6,
            handler='index.handler',
            code=Code.from_inline('def handler(*args, **kwargs): return 200')
        )

        bucket.add_object_created_notification(LambdaDestination(function))
