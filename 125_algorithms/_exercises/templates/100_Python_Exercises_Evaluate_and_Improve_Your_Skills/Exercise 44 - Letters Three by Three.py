#FromScratch - Create a script that generates a file where all letters of English alphabet are listed three in each line

______ string

letters _ string.ascii_lowercase + " "

slice1 _ letters[0::3]
slice2 _ letters[1::3]
slice3 _ letters[2::3]

w__ o..("letters.txt", _) __ file:
    ___ s1, s2, s3 __ zip(slice1, slice2, slice3):
        print(s1, s2, s3)
        file.w..(s1 + s2 + s3 + "\n")
