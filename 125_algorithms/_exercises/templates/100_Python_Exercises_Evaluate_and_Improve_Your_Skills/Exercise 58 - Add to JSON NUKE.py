#Add a new employee to the json file.

_______ json

with open("company1.json", "r+") as file:
    d  json.loads(file.read())
    d["employees"].a..(d..(firstName  "Albert", lastName  "Bert"))
    file.seek(0)
    json.dump(d, file, indent4, sort_keysTrue)
    file.truncate()
