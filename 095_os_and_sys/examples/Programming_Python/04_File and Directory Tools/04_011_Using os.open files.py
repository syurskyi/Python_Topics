import sys
for stream in (sys.stdin, sys.stdout, sys.stderr):
    print(stream.fileno())
# 012
# ######################################################################################################################

sys.stdout.write('Hello stdio world\n') # write via file method
# Hello stdio world
# 18
# ######################################################################################################################

import os
os.write(1, b'Hello descriptor world\n') # write via os module
# Hello descriptor world
# 23
# ######################################################################################################################

file = open(r'C:\temp\spam.txt', 'w') # create external file, object
file.write('Hello stdio file\n') # write via file object method
file.flush() # else os.write to disk first!
fd = file.fileno() # get descriptor from object
fd
# 3
# ######################################################################################################################

import os
os.write(fd, b'Hello descriptor file\n') # write via os module
file.close()
# C:\temp> type spam.txt # lines from both schemes
# Hello stdio file
# Hello descriptor file
# ######################################################################################################################

