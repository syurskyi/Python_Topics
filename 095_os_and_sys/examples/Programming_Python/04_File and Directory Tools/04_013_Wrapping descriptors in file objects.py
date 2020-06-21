import os
fdfile = os.open(r'C:\temp\spam.txt', (os.O_RDWR | os.O_BINARY))
fdfile
# 3
# ######################################################################################################################

objfile = os.fdopen(fdfile, 'rb')
objfile.read()
# b'Jello stdio file\r\nHello descriptor file\n'
# ######################################################################################################################

# C:\...\PP4E\System> python
import os
fdfile = os.open(r'C:\temp\spam.txt', (os.O_RDWR | os.O_BINARY))
objfile = os.fdopen(fdfile, 'r')
objfile.read()
# 'Jello stdio file\nHello descriptor file\n'
# ######################################################################################################################

# C:\...\PP4E\System> python
import os
fdfile = os.open(r'C:\temp\spam.txt', (os.O_RDWR | os.O_BINARY))
fdfile
# 3
# ######################################################################################################################

objfile = open(fdfile, 'r', encoding='latin1', closefd=False)
objfile.read()
# 'Jello stdio file\nHello descriptor file\n'
# ######################################################################################################################

objfile = os.fdopen(fdfile, 'r', encoding='latin1', closefd=True)
objfile.seek(0)
objfile.read()
# 'Jello stdio file\nHello descriptor file\n'
# ######################################################################################################################