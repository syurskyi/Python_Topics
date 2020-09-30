#Write a script that extracts letters from the 26 text files and put the letters in a list
import glob

letters =   # list
file_list = glob.glob("letters/*.txt")
print(file_list)
___ filename __ file_list:
    with open(filename, "r") as file:
        letters.append(file.read().strip("\n"))

print(letters)
