# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to find all five characters long word in a string.
# Input
# 'The quick brown fox jumps over the lazy dog.'
# Output
# ['quick', 'brown', 'jumps']

import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.findall(r"\b\w{5}\b", text))


