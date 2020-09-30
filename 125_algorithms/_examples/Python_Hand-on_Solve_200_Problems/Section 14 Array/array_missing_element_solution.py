# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ----------------------------------------------------------------
# Consider an array of non-negative integers.
# A second array is formed by shuffling the elements of the first array and deleting a random element. 
# Given these two arrays, find which element is missing in the second array.
# Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.
# Input:
# finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# Output:
# 5 is the missing number
# ----------------------------------------------------------------
# Algorithm
# 
# ----------------------------------------------------------------


first_array = [1,2,3,4,5,6,7]
second_array = [3,7,2,1,4,6]

def finder(first_array, second_array):
    return(sum(first_array) - sum(second_array))

missing_number = finder(first_array, second_array)

print(missing_number)    


