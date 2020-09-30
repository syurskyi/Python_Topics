# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program for binary search. 
# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target value
# within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and 
# executes in logarithmic time.

def binary_search(item_listac,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


