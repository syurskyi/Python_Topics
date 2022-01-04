#Write a script that extracts letters from the 26 text files and put the letters in a list
_______ glob

letters  []
file_list  glob.glob("letters/*.txt")
print(file_list)
___ filename __ file_list:
    with open(filename, "r") __ file:
        letters.a..(file.read().strip("\n"))

print(letters)
