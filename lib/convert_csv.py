import json, csv, sys

csv_file_path = 'explorecards.csv'
json_file_path = 'explorecards.json'

data = []
with open(csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)
    
with open(json_file_path, 'w') as json_file:
    json_file.write(json.dumps(data, indent=4))