# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to get the factorial of a non-negative integer.

def factorial(n):
  if n <= 1:
    return 1
  else:
    return n * (factorial(n - 1))
    
print(factorial(5))


