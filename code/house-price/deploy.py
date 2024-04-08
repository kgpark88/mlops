import mlflow.sagemaker
from mlflow.deployments import get_deploy_client

endpoint_name="prod-endpoint"
model_uri = "s3://mlflow-project-artifacts-danny1214/2/17e1881c9da1497a8a43f61c2d173c59/artifacts/Ridge"

# Define your configuration parameters as a dictionary
config = {
    "execution_role_arn": "arn:aws:iam::730335301614:role/house-price-role",
    "bucket_name": "mlflow-project-artifacts-danny1214",
    "image_url": "730335301614.dkr.ecr.ap-northeast-2.amazonaws.com/ridge:2.11.3",
    "region_name": "ap-northeast-2",
    "archive": False,
    "instance_type": "ml.m5.large",
    "instance_count": 1,
    "synchronous": True,
}

# Initialize a deployment client for SageMaker
client = get_deploy_client("sagemaker")

# Create the deployment
client.create_deployment(
    name=endpoint_name,
    model_uri=model_uri,
    flavor="python_function",
    config=config,
)
