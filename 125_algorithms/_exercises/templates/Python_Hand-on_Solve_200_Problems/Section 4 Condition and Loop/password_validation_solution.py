# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to check the validity of a password (input from users).

# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

# Input
# W3r@100a
# Output
# Valid password

______ __
p_ i..("Input your password")
x _ T..
w___ x:  
    __ (le.(p)<6 or le.(p)>12):
        b..
    ____ no. __.s..("[a-z]",p):
        b..
    ____ no. __.s..("[0-9]",p):
        b..
    ____ no. __.s..("[A-Z]",p):
        b..
    ____ no. __.s..("[$#@]",p):
        b..
    ____ __.s..("\s",p):
        b..
    ____
        print("Valid Password")
        x_False
        b..

__ x:
    print("Not a Valid Password")


