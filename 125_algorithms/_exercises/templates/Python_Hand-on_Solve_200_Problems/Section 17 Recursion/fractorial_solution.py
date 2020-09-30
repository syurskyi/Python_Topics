# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to get the factorial of a non-negative integer.

___ factorial(n):
  __ n <_ 1:
    r_ 1
  ____
    r_ n * (factorial(n - 1))
    
print(factorial(5))


