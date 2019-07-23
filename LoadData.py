from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('News')

with open("data.json") as json_file:
    news = json.load(json_file)
    for (headline) in news.items():
        print(headline)
    for news in news:
        Headline = news[0]

        print("Adding headline:", Headline)

        table.put_item(
           Item={
               'year': Headline,
            }
        )
