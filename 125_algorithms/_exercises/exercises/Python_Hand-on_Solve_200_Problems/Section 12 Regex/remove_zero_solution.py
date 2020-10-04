# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to remove leading zeros from an IP address.
# Input
# "216.08.094.196"
# Output
# 216.8.94.196

______ __
ip _ "216.08.094.196"
string _ __.sub '\.[0]*', '.', ip
print string


