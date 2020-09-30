#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Print out message "Passowrd is not fine" if the user didn't create a correct password

while T..:
    psw _ input("Enter new password: ")
    __ any(i.isdigit() ___ i __ psw) an. any(i.isupper() ___ i __ psw) an. le.(psw) >_ 5:
        print("Password is fine")
        break
    ____
        print("Passowrd is not fine")
