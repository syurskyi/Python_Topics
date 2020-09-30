str1 _ input("Insert starting letter: ")
str2 _ input("Insert ending letter: ")

while str1 <_ str2:
    print(str1, end_" ")
    str1 _ chr(ord(str1) + 1)
print()
