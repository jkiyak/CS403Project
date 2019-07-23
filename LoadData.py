from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('News')

with open("data.json") as json_file:
    news = json.load(json_file, parse_float = decimal.Decimal)
    for eachnews in news:
        year = eachnews[0]
        title = eachnews[1]

        print("Adding headline:", year, title)

        table.put_item(
           Item={
               'year': year,
               'title': title,
            }
        )
