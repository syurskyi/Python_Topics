#Write a script that extracts letters from the 26 text files and put the letters in a list
______ glob

letters _   # list
file_list _ glob.glob("letters/*.txt")
print(file_list)
___ filename __ file_list:
    with open(filename, "r") as file:
        letters.ap..(file.read().strip("\n"))

print(letters)
