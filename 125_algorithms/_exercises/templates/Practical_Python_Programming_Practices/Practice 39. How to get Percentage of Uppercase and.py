st. _ input("Insert some strings of Uppercase and Lowercase: ")

len_str _ le.(st.)

upper _ lower _ 0

___ i __ st.:
    __ 'a' <_ i <_ 'z':
        lower +_ 1
    elif 'A' <_ i <_ 'Z':
        upper +_ 1

print("Percentage of Uppercase: %.2f %%" % (upper/len_str * 100))
print("Percentage of Lowercase: %.2f %%" % (lower/len_str * 100))