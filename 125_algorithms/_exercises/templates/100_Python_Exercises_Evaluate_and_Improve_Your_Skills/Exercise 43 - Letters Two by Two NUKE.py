#Create a script that generates a file where all letters of English alphabet are listed two in each line

_______ string

with open("letters.txt", "w") as file:
    ___ letter1, letter2 __ zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        file.write(letter1 + letter2 + "\n")
