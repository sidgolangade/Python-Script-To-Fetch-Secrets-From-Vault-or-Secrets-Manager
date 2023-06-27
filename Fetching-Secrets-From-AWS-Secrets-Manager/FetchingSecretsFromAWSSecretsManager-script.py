import boto3

def fetch_secret(secret_name, region_name):
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    
    response = client.get_secret_value(SecretId=secret_name)
    secret_value = response['SecretString']
    
    return secret_value

def write_to_file(secret_value, output_file):
    with open(output_file, 'w') as file:
        file.write(secret_value)

# Set your secret name and region here
secret_name = input("Enter the Secret Name: ")
region_name = input("Enter the Region Name: ")

# Set the output file path here
output_file = 'secret-output.txt'

# Fetch the secret value from AWS Secrets Manager
secret_value = fetch_secret(secret_name, region_name)

# Write the secret value to the output file
write_to_file(secret_value, output_file)

print(f"Secret value fetched and stored in {output_file} successfully.")
