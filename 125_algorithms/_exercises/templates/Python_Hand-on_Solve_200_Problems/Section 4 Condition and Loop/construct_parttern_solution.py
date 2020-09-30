# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
#  Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n=5;
___ i __ range(n):
    ___ j __ range(i):
        print ('* ', end="")
    print('')

___ i __ range(n,0,-1):
    ___ j __ range(i):
        print('* ', end="")
    print('')
	

