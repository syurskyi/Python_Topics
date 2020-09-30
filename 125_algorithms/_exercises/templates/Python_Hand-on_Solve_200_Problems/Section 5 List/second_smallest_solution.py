# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to find the second smallest number in a list.
# input
# second_smallest([1, 2, -8, -2, 0])
# output
# -2

___ second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    ___ x __ numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    r_ a2

print(second_smallest([1, 2, -8, -2, 0]))


