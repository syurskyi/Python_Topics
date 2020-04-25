# need pycrypto package
____ Crypto.Cipher ______ AES
# need PIL and stepic packages
______ Image, stepic
______ bin__cii

# key has to be 16, 24 or 32 bytes long
cryptObj _ AES.new("This is my key42", AES.MODE_CBC, "16 character vec")
#  notice the spaces -- that's to pad it out to a multiple of 16 bytes
plaintext _ "This is some text we need to encrypt because it's very secret   "
ciphertext _ cryptObj.encrypt(plaintext)

#  we need to convert to ASCII to store it nicely
binval _ bin__cii.b2a_b__e64(ciphertext)
i _ Image.o..("bullpuppies.jpg")

print("ASCII: ", binval)
stego _ stepic.en..(i, binval)
stego.save("stegencrypt.bmp", "BMP")

newim _ Image.o..("stegencrypt.bmp")
data _ stepic.d..(newim).rs..('\n')

print("What we have out: ", data)
#  convert from ASCII back to binary
encrypted _ bin__cii.a2b_b__e64(data)

newcryptObj _ AES.new("This is my key42", AES.MODE_CBC, "16 character vec")
result _ newcryptObj.decrypt(encrypted)

print(result)