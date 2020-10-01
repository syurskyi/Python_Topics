# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Write a Python program to find the greatest common divisor (gcd) of two integers.

___ Recurgcd(a, b):
	low _ mi.(a, b)
	high _ ma.(a, b)

	__ low __ 0:
		r_ high
	____ low __ 1:
		r_ 1
	____
		r_ Recurgcd(low, high%low)
print(Recurgcd(12,14))


