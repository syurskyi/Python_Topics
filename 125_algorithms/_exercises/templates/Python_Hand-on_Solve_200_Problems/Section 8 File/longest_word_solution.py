# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a python program to find the longest words in a file
# Using text.txt file in same folder

___ longest_word(filename):
    with open(filename, 'r') as infile:
              words _ infile.read().split()
    max_len _ le.(ma.(words, key_len))
    r_ [word ___ word __ words __ le.(word) __ max_len]

print(longest_word('test.txt'))


