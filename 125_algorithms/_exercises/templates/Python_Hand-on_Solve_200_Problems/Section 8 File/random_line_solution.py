# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to read a random line from a file.
# Using test.txt

______ random

___ random_line(fname):
    lines _ open(fname).read().splitlines()
    r_ random.choice(lines)
print(random_line('test.txt'))


