#Write a script that extracts letters from files if letters are contained in "python" and puts the letters in a list
______ glob

letters _   # list
file_list _ glob.iglob("letters/*.txt")
check _ "python"

___ filename __ file_list:
    with open(filename,"r") as file:
        letter _ file.read().strip("\n")
        __ letter __ check:
            letters.ap..(letter)

print(letters)
