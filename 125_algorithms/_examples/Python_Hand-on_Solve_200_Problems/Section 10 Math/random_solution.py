# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#  Write a Python program to generate a series of unique random numbers

import random

choices = list(range(100))
random.shuffle(choices)
print(choices.pop())
while choices:
    print(choices.pop())


