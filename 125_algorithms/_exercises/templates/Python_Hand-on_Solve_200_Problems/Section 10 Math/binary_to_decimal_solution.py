# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to convert a binary number to decimal number.


b_num = list(input("Input a binary number: "))
value = 0

___ i __ range(len(b_num)):
	digit = b_num.pop()
	if digit == '1':
		value = value + pow(2, i)
print("The decimal value of the number is", value)


