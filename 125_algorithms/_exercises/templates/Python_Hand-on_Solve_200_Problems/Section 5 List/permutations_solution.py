# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#  Write a Python program to generate all permutations of a list in Python
# Input [1,2,3]
# Output [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

import itertools
print(list(itertools.permutations([1,2,3])))


