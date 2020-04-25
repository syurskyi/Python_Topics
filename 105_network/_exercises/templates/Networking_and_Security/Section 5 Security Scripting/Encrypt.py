# need pycrypto package
____ Crypto.Cipher ______ AES

# key has to be 16, 24 or 32 bytes long
cryptObj _ AES.new("This is my key42", AES.MODE_CBC, "16 character vec")
#  notice the spaces -- that's to pad it out to a multiple of 16 bytes
plaintext _ "This is some text we need to encrypt because it's very secret   "
ciphertext _ cryptObj.encrypt(plaintext)
print("Cipher text: ", ciphertext)

# this won't work if the key isn't identical
newcryptObj _ AES.new("This is my key42", AES.MODE_CBC, "16 character vec")
result _ newcryptObj.decrypt(ciphertext)

print(result)