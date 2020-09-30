# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).
# Input
# "ABCDEFabcdef123450"
# "*&%@#!}{"
# Output
# True                                                                                                          
# False

______ __
___ is_allowed_specific_char(string):
    charRe _ __.c..(r'[^a-zA-Z0-9.]')
    string _ charRe.s..(string)
    r_ not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))


