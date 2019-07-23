import json

with open('Data.json') as data_file:    
    data = json.load(data_file)
    for news in data:
        print (data)
