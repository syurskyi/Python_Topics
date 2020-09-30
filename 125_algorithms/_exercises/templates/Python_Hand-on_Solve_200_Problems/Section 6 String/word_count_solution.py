# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#  Write a Python program to count the occurrences of each word in a given sentence

___ word_count(str):
    counts = dict()
    words = str.split()

    ___ word __ words:
        if word __ counts:
            counts[word] += 1
        else:
            counts[word] = 1

    r_ counts

print( word_count('the quick brown fox jumps over the lazy dog.'))


