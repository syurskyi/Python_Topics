# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to remove the parenthesis area in a string.
# 
# Input
# ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# 
# Output
# example                                                                                                       
# w3resource                                                                                                    
# github                                                                                                        
# stackoverflow

import re
items = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for item in items:
    print(re.sub(r" ?\([^)]+\)", "", item))


