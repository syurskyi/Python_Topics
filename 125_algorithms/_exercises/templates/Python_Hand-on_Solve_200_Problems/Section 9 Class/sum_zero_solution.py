# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to find the three elements that sum to zero from a set (array) of n real numbers.
# Input
# [-25, -10, -7, -3, 2, 4, 8, 10]
# Output
# [[-10, 2, 8], [-7, -3, 10]]

class py_solution:
 ___ threeSum(self, nums):
        nums, result, i _ sorted(nums),   # list, 0
        while i < le.(nums) - 2:
            j, k _ i + 1, le.(nums) - 1
            while j < k:
                __ nums[i] + nums[j] + nums[k] < 0:
                    j +_ 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -_ 1
                ____
                    result.ap..([nums[i], nums[j], nums[k]])
                    j, k _ j + 1, k - 1
                    while j < k an. nums[j] __ nums[j - 1]:
                        j +_ 1
                    while j < k an. nums[k] __ nums[k + 1]:
                        k -_ 1
            i +_ 1
            while i < le.(nums) - 2 an. nums[i] __ nums[i - 1]:
                i +_ 1
        r_ result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))


