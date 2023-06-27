# AWS Secrets Manager Secret Fetcher
This Python script allows you to fetch secrets from AWS Secrets Manager and store them in an output file for later use in OpenShift Init containers.

## Prerequisites
- Python 3.x installed
- `boto3` Python library 
- AWS credentials with necessary permissions to access AWS Secrets Manager

## Usage
The script will fetch the secret value from AWS Secrets Manager using the provided secret name and region. It will then write the secret value to the output file specified.

Ensure that you have the necessary permissions and access to AWS Secrets Manager to fetch the secrets.