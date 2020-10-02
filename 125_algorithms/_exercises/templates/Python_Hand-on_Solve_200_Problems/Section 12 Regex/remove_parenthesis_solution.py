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

______ __
i.. _ ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
___ item __ i..:
    print __.sub r" ?\([^)]+\)", "", item


