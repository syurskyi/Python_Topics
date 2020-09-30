#Create a script that lets the user create a password until they have satisfied three conditions:
#Password contains at least one number, one uppercase letter and it is at least 5 chars long
#Give the exact reason why the user has not created a correct password
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

#Video question -Experienced
#Video solution -Experienced
