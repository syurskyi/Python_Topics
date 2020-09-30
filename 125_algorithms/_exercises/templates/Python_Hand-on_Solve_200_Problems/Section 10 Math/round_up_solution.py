# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python function to round up a number to specified digits.

______ math

___ roundup(a, digits_0):
    n _ 10**-digits
    r_ round(math.ceil(a / n) * n, digits)

x _ 123.01247
print("Original  Number: ",x)
print(roundup(x, 0))
print(roundup(x, 1))
print(roundup(x, 2))
print(roundup(x, 3))


