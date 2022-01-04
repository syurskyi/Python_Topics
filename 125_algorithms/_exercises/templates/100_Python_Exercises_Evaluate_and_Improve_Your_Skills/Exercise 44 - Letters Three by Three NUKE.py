#FromScratch - Create a script that generates a file where all letters of English alphabet are listed three in each line

_______ string

letters  string.ascii_lowercase + " "

slice1  letters[0::3]
slice2  letters[1::3]
slice3  letters[2::3]

with open("letters.txt", "w") __ file:
    ___ s1, s2, s3 __ z..(slice1, slice2, slice3):
        print(s1, s2, s3)
        file.write(s1 + s2 + s3 + "\n")
