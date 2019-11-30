file = open('data.txt', 'wb') # open binary output file
file = open('data.txt', 'rb') # open binary input file

# 'Hello file world!\nBye file world.\nThe Life of Brian'
# ######################################################################################################################

open('data.txt', 'rb').read() # binary mode: bytes
# b'Hello file world!\r\nBye file world.\r\nThe Life of Brian'
# ######################################################################################################################

file = open('data.txt', 'rb')
for line in file: print(line)

# b'Hello file world!\r\n'
# b'Bye file world.\r\n'
# b'The Life of Brian'
# ######################################################################################################################

open('data.bin', 'wb').write(b'Spam\n')
# 5
# ######################################################################################################################

open('data.bin', 'rb').read()
# b'Spam\n'
# ######################################################################################################################

open('data.bin', 'wb').write('spam\n')
# TypeError: must be bytes or buffer, not str
# ######################################################################################################################

