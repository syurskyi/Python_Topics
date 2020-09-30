# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to find urls in a string.
# 
# Input
# '<p>Contents :</p><a href="https://www.w3schools.com/html/">Python Examples</a><a href="http://github.com">Even More Examples</a>'
# 
# Output
# Urls:  ['https://w3resource.com', 'http://github.com']

import re
text = '<p>Contents :</p><a href="https://w3resource.com">Python Examples</a><a href="http://github.com">Even More Examples</a>'
urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
print("Original string: ",text)
print("Urls: ",urls)


