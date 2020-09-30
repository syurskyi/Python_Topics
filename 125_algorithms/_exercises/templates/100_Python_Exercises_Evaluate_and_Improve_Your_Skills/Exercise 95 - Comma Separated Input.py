#Create a program that asks the user to input values separated by commas and those values will be stored in a separate line each in a text file

line _ input("Enter values: ")

line_list _ line.split(",")

w__ o..("user_data_commas.txt", "a+") __ file:
    ___ i __ line_list:
        file.w..(i + "\n")

#Video question -Intermediate
