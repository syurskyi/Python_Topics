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

______ re
p_ input("Input your password")
x _ T..
while x:  
    __ (le.(p)<6 or le.(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    ____
        print("Valid Password")
        x_False
        break

__ x:
    print("Not a Valid Password")


