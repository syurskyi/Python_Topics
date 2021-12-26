import json

with open("file2.txt") as json_file:
    data = json.load(json_file)
    print(data["metals"]["steel"]["density"])
