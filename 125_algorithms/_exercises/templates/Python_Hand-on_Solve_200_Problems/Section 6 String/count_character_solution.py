# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google'
# Expected Result : {'g': 2, 'o': 2, 'l': 1, 'e': 1}

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency('google'))


