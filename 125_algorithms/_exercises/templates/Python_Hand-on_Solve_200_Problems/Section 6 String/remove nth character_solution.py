# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to remove the nth index character from a nonempty string

___ remove_char(st., n):
      first_part _ st.[:n]
      last_pasrt _ st.[n+1:]
      r_ first_part + last_pasrt
    
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))


