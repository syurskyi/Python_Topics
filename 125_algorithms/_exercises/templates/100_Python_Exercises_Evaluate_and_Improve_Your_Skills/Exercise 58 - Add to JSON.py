#Add a new employee to the json file.

______ ____

w__ o..("company1.json", "r+") __ file:
    d _ ____.loads(file.read
    d["employees"].ap..(di..(firstName _ "Albert", lastName _ "Bert"))
    file.seek(0)
    ____.d..(d, file, indent_4, sort_keys_True)
    file.truncate()
