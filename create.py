import boto3

client = boto3.client('dynamodb', region_name='us-east-1')

resp = client.create_table(
    TableName="Urls",
    KeySchema=[
        {
            "AttributeName": "Reduction",
            "KeyType": "HASH"
        },
        {
            "AttributeName": "URL",
            "KeyType": "RANGE"
        }
    ],
    AttributeDefinitions=[
        {
            "AttributeName": "Reduction",
            "AttributeType": "S"
        },
        {
            "AttributeName": "URL",
            "AttributeType": "S"
        }
    ],
    ProvisionedThroughput={
        "WriteCapacityUnits": 1,
        "ReadCapacityUnits": 1
    }
)
