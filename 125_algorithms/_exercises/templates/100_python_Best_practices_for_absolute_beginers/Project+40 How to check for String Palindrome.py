s..   input("Insert a string: ")
len_str  l..(s..)

___ i __ r..(len_str//2):
    __ s..[i] ! s..[-1-i]:
        print("This is NOT a palindrome!")
        quit()
print("This is a PALINDROME!")