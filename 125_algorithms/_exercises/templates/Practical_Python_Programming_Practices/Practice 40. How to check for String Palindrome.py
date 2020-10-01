st.  _ i..("Insert a string: ")
len_str _ le.(st.)

___ i __ ra..(len_str//2):
    __ st.[i] !_ st.[-1-i]:
        print("This is NOT a palindrome!")
        quit()
print("This is a PALINDROME!")