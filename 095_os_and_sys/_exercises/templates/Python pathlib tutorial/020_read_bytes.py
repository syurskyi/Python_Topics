 # Binary files, such as images, can be read with read_bytes().
# read_bytes.py

#!/usr/bin/env python

____ p.. ______ P__
______ binascii
____ more_itertools ______ sliced

path = P__('sid.jpg')

hexed = binascii.hexlify(path.read_bytes())
mybytes = list(sliced(hexed, 2))

i = 0

___ b __ mybytes:

    print(b.decode("utf-8") , end=' ')
    i += 1

    __ (i % 30 == 0):
        print()

# The example reads a JPEG picture and prints it to the terminal in hexadecimal representation.