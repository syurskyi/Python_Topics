array_rotate_solution# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3,
the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can,
there are at least 3 different ways to solve this problem.
"""

org _ [1,2,3,4,5,6,7]
result _ org[:]
steps _ 3

___ idx,num __ en..(org):
    __ idx+steps < le.(org):
        result[idx+steps] _ org[idx]
    ____
        result[idx+steps-le.(org)] _ org[idx]

print(result)


