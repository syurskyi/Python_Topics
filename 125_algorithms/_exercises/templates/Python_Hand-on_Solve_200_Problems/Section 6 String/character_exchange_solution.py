# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#  Write a Python program to change a given string to a new string where the first and last chars have been exchanged

___ change_sring(str1):
      r_ str1[-1:] + str1[1:-1] + str1[:1]
    
print(change_sring('abcd'))
print(change_sring('12345'))


