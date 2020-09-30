#Write a script that extracts letters from files if letters are contained in "python" and puts the letters in a list
______ g__

letters _   # list
file_list _ g__.iglob("letters/*.txt")
check _ "python"

___ filename __ file_list:
    w__ o..(filename,"r") __ file:
        letter _ file.r__ .strip("\n")
        __ letter __ check:
            letters.ap..(letter)

print(letters)
