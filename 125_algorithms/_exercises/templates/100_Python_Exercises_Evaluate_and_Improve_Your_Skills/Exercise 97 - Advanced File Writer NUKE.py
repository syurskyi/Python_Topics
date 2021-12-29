#Create a program that asks the user to submit text through a GUI

file  open("user_data_save_close.txt", 'a+')

w___ T...
    line  input("Write a value: ")
    __ line __ "SAVE":
        file.close()
        file  open("user_data_save_close.txt", 'a+')
    elif line __ "CLOSE":
        file.close()
        _____
    else:
        file.write(line + "\n")
