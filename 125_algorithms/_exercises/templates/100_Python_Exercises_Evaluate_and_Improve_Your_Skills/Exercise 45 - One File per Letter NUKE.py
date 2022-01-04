#Create a script that generates 26 text files, each containing one letter of English alphabet as a name and as text inside.

_______ string, os

__ n.. os.path.exists("letters"):
    os.makedirs("letters")
___ letter __ string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") __ file:
        file.write(letter + "\n")
