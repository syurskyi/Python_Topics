#Create a script that generates 26 text files, each containing one letter of English alphabet as a name and as text inside.

______ string, os

__ not os.path.exists("letters"):
    os.makedirs("letters")
___ letter __ string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")
