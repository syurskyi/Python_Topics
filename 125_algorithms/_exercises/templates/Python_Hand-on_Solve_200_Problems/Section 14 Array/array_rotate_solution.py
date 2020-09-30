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

org = [1,2,3,4,5,6,7]
result = org[:]
steps = 3

for idx,num in enumerate(org):
    if idx+steps < len(org):
        result[idx+steps] = org[idx]
    else:
        result[idx+steps-len(org)] = org[idx]

print(result)


