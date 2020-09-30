# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to calculate the value of 'a' to the power 'b'.

___ power(a,b):
	if b==0:
		r_ 1
	elif a==0:
		r_ 0
	elif b==1:
		r_ a
	else:
		r_ a*power(a,b-1)

print(power(3,4))


