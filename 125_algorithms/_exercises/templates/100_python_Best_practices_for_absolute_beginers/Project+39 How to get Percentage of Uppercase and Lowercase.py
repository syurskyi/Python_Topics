str  input("Insert some strings of Uppercase and Lowercase: ")

len_str  l..(str)

upper  lower  0

___ i __ str:
    __ 'a' < i < 'z':
        lower + 1
    ____ 'A' < i < 'Z':
        upper + 1

print("Percentage of Uppercase: %.2f %%" % (upper/len_str * 100))
print("Percentage of Lowercase: %.2f %%" % (lower/len_str * 100))