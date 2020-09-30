#Create a program that asks the user to submit text through a GUI

file _ open("user_data_save_close.txt", 'a+')

while T..:
    line _ input("Write a value: ")
    __ line __ "SAVE":
        file.close()
        file _ open("user_data_save_close.txt", 'a+')
    elif line __ "CLOSE":
        file.close()
        break
    ____
        file.write(line + "\n")
