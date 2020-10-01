# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# ---------------------------------------------------------------
# python best courses https://courses.tanpham.org/
# ---------------------------------------------------------------
# Write a Python program to create a Caesar encryption

# Note : In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
# It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
# The method is named after Julius Caesar, who used it in his private correspondence.

# plaintext:  defend the east wall of the castle
# ciphertext: efgfoe uif fbtu xbmm pg uif dbtumf

___ caesar_encrypt(realText, step):
	outText _   # list
	cryptText _   # list
	
	uppercase _ ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase _ ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	___ eachLetter __ realText:
		__ eachLetter __ uppercase:
			index _ uppercase.index(eachLetter)
			crypting _ (index + step) % 26
			cryptText.ap..(crypting)
			newLetter _ uppercase[crypting]
			outText.ap..(newLetter)
		____ eachLetter __ lowercase:
			index _ lowercase.index(eachLetter)
			crypting _ (index + step) % 26
			cryptText.ap..(crypting)
			newLetter _ lowercase[crypting]
			outText.ap..(newLetter)
	r_ outText

code _ caesar_encrypt('defend the east wall of the castle', 1)
print()
print(code)
print()


