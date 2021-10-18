 # Binary files, such as images, can be read with read_bytes().
# read_bytes.py

#!/usr/bin/env python

from pathlib import Path
import binascii
from more_itertools import sliced

path = Path('sid.jpg')

hexed = binascii.hexlify(path.read_bytes())
mybytes = list(sliced(hexed, 2))

i = 0

for b in mybytes:

    print(b.decode("utf-8") , end=' ')
    i += 1

    if (i % 30 == 0):
        print()

# The example reads a JPEG picture and prints it to the terminal in hexadecimal representation.