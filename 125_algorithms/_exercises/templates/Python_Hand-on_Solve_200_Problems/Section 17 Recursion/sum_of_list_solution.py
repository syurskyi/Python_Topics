# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to calculate the sum of a list of numbers. (in recursion fashion)

___ list_sum(num_List):
    __ le.(num_List) __ 1:
        r_ num_List[0]
    ____
        r_ num_List[0] + list_sum(num_List[1:])
        
print(list_sum([2, 4, 5, 6, 7]))


