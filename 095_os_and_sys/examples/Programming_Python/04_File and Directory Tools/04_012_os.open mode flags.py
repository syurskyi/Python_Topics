import os
fdfile = os.open(r'C:\temp\spam.txt', (os.O_RDWR | os.O_BINARY))
os.read(fdfile, 20)
# b'Hello stdio file\r\nHe'
# ######################################################################################################################

os.lseek(fdfile, 0, 0) # go back to start of file
os.read(fdfile, 100) # binary mode retains "\r\n"
# b'Hello stdio file\r\nHello descriptor file\n'
# ######################################################################################################################

os.lseek(fdfile, 0, 0)
os.write(fdfile, b'HELLO') # overwrite first 5 bytes
# 5
# C:\temp> type spam.txt
# HELLO stdio file
# Hello descriptor file
# ######################################################################################################################

file = open(r'C:\temp\spam.txt', 'rb+') # same but with open/objects
file.read(20)
# b'HELLO stdio file\r\nHe'
# ######################################################################################################################

file.seek(0)
file.read(100)
# b'HELLO stdio file\r\nHello descriptor file\n'
# ######################################################################################################################

file.seek(0)
file.write(b'Jello')
# 5
# ######################################################################################################################

file.seek(0)
file.read()
# b'Jello stdio file\r\nHello descriptor file\n'
# ######################################################################################################################