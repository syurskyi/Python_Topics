#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

file  open("user_data.txt", 'a+')

w___ T...
    line  input("Write a value: ")
    __ line __ "CLOSE":
        file.close()
        _____
    ____:
        file.write(line + "\n")
