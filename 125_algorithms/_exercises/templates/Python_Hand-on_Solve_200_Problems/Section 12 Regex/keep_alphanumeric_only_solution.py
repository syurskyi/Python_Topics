# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to remove everything except alphanumeric characters from a string.
# Input
# '**//Python Exercises// - 12. '
# Output
# PythonExercises12

______ __
text1 _ '**//Python Exercises// - 12. '
pattern _ __.c..('[\W_]+')
print(pattern.sub('', text1))


