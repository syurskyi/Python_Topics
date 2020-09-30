______ json

___ foo(metal, property, filepath):
    with open(filepath) as json_file:
        data _ json.load(json_file)
        r_ data["metals"][metal][property]
