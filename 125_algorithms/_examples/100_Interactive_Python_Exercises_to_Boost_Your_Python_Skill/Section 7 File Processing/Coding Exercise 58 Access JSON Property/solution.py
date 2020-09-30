import json

def foo(metal, property, filepath):
    with open(filepath) as json_file:
        data = json.load(json_file)
        return data["metals"][metal][property]
