#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

file _ o..("user_data.txt", 'a+')

while T..:
    line _ input("Write a value: ")
    __ line __ "CLOSE":
        file.c..
        break
    ____
        file.w..(line + "\n")
