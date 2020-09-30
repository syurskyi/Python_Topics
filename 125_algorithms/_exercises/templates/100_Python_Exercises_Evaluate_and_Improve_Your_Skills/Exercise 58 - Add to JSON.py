#Add a new employee to the json file.

______ json

with open("company1.json", "r+") as file:
    d _ json.loads(file.read
    d["employees"].ap..(di..(firstName _ "Albert", lastName _ "Bert"))
    file.seek(0)
    json.dump(d, file, indent_4, sort_keys_True)
    file.truncate()
