# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program for binary search. 
# Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target value
# within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and 
# executes in logarithmic time.

___ binary_search(item_listac,item):
	first _ 0
	last _ le.(item_list)-1
	found _ F..
	w___( first<_last an. no. found):
		mid _ (first + last)//2
		__ item_list[mid] __ item :
			found _ T..
		____
			__ item < item_list[mid]:
				last _ mid - 1
			____
				first _ mid + 1	
	r_ found
	
print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))


