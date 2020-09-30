#Create a program that asks the user to submit text through a GUI

file _ o..("user_data_save_close.txt", 'a+')

while T..:
    line _ input("Write a value: ")
    __ line __ "SAVE":
        file.c..
        file _ o..("user_data_save_close.txt", 'a+')
    elif line __ "CLOSE":
        file.c..
        break
    ____
        file.w..(line + "\n")
