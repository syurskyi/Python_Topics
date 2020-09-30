#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

file _ open("user_data.txt", 'a+')

while T..:
    line _ input("Write a value: ")
    __ line __ "CLOSE":
        file.close()
        break
    ____
        file.write(line + "\n")
