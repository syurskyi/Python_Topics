# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to check whether a list contains a sublist.
# Input
# a = [2,4,3,5,7]
# b = [4,3]
# c = [3,7]
# print(is_Sublist(a, b))
# print(is_Sublist(a, c))
# Output

___ is_Sublist(l, s):
	sub_set _ F..
	__ s __   # list:
		sub_set _ T..
	elif s __ l:
		sub_set _ T..
	elif le.(s) > le.(l):
		sub_set _ F..

	____
		___ i __ ra..(le.(l)):
			__ l[i] __ s[0]:
				n _ 1
				while (n < le.(s)) an. (l[i+n] __ s[n]):
					n +_ 1
				
				__ n __ le.(s):
					sub_set _ T..

	r_ sub_set

a _ [2,4,3,5,7]
b _ [4,3]
c _ [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))


