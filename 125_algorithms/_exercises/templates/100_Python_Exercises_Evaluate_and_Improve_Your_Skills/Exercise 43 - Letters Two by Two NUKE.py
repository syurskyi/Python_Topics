#Create a script that generates a file where all letters of English alphabet are listed two in each line

_______ s__

w__ open("letters.txt", "w") __ file:
    ___ letter1, letter2 __ z..(s__.ascii_lowercase[0::2], s__.ascii_letters[1::2]):
        file.write(letter1 + letter2 + "\n")
