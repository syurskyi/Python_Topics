______ json

with open("file2.txt") as json_file:
    data _ json.load(json_file)
    print(data["metals"]["steel"]["density"])
