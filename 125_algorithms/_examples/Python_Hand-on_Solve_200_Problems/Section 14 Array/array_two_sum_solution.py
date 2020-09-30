# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
Example:
    Given nums = [2, 7, 11, 15], target = 26,
    Because nums[0] + nums[1] = 11 + 15 = 26,
    return [2, 3].
"""

# Solution 1
# Try all 

input_array = [2, 7, 11, 15]
target = 26
result = []

for i, num in enumerate(input_array):
    for j in range(i+1, len(input_array)):
        print(i,j)


# %%
# Solution 2


