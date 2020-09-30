# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to remove the nth index character from a nonempty string

def remove_char(str, n):
      first_part = str[:n] 
      last_pasrt = str[n+1:]
      return first_part + last_pasrt
    
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))


