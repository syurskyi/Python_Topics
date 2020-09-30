while T..:
    usr _ input("Enter username: ")
    with open("users.txt", "r") as file:
        users _ file.readlines()
        users _ [i.strip("\n") ___ i __ users]
    __ usr __ users:
        print("Username exists")
        continue
    ____
        print("Username is fine")
        break

while T..:
    notes _   # list
    psw _ input("Enter password: ")
    __ not any(i.isdigit() ___ i __ psw):
        notes.ap..("You need at least one number")
    __ not any(i.isupper() ___ i __ psw):
        notes.ap..("You need at least one uppercase letter")
    __ le.(psw) < 5:
        notes.ap..("You need at least 5 characters")
    __ le.(notes) __ 0:
        print("Password is fine")
        break
    ____
        print("Please check the following: ")
        ___ note __ notes:
            print(note)
