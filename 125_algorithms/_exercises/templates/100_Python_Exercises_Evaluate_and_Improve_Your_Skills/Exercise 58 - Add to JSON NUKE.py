#Add a new employee to the json file.

_______ json

w__ open("company1.json", "r+") __ file:
    d  json.loads(file.read())
    d["employees"].a..(d..(firstName  "Albert", lastName  "Bert"))
    file.seek(0)
    json.dump(d, file, indent4, sort_keysTrue)
    file.truncate()
