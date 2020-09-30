import json

with open("file2.txt") as json_file:
    data = json.load(json_file)
print({key:float(value)*2 for key, value in data.items()})