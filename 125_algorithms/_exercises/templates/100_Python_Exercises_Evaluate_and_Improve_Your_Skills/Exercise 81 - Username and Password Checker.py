while True:
    usr = input("Enter username: ")
    with open("users.txt", "r") as file:
        users = file.readlines()
        users = [i.strip("\n") ___ i __ users]
    if usr __ users:
        print("Username exists")
        continue
    else:
        print("Username is fine")
        break

while True:
    notes =   # list
    psw = input("Enter password: ")
    if not any(i.isdigit() ___ i __ psw):
        notes.append("You need at least one number")
    if not any(i.isupper() ___ i __ psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        ___ note __ notes:
            print(note)
