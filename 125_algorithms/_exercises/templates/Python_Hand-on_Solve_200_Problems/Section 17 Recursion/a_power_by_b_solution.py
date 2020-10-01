# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to calculate the value of 'a' to the power 'b'.

___ power(a,b):
	__ b__0:
		r_ 1
	____ a__0:
		r_ 0
	____ b__1:
		r_ a
	____
		r_ a*power(a,b-1)

print(power(3,4))


