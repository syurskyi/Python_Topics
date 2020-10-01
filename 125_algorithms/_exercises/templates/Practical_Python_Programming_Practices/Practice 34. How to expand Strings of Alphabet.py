str1 _ i..("Insert starting letter: ")
str2 _ i..("Insert ending letter: ")

w___ str1 <_ str2:
    print(str1, end_" ")
    str1 _ chr(ord(str1) + 1)
print()
