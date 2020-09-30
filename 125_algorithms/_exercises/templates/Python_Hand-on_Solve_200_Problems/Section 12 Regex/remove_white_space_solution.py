# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Remove all whitespaces from a string
# 
# Input
# ' Python    Exercises '
# Output
# PythonExercises

import re
text1 = ' Python    Exercises '
print("Original string:",text1)
print("Without extra spaces:",re.sub(r'\s+', '',text1))


