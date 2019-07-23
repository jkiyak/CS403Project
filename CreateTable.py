from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')


table = dynamodb.create_table(
    TableName='News',
    KeySchema=[
        {
            'AttributeName': 'Headline',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'img',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Headline',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'img',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)
