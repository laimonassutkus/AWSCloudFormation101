from setuptools import setup, find_packages

setup(
    name='workshop',
    version='0.0.1',
    packages=find_packages(exclude=['venv']),
    description='Workshop for AWS CDK tool.',
    include_package_data=True,
    install_requires=[
        "aws-cdk.core==1.91.0",
        "aws-cdk.aws-s3==1.91.0",
        "aws-cdk.aws-lambda==1.91.0",
        "aws-cdk.aws_s3_notifications==1.91.0",
    ]
)
