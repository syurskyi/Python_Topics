#Write a script that extracts letters from files if letters are contained in "python" and puts the letters in a list
import glob

letters =   # list
file_list = glob.iglob("letters/*.txt")
check = "python"

___ filename __ file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
        if letter __ check:
            letters.append(letter)

print(letters)
