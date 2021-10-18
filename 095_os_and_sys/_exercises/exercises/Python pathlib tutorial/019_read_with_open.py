 # The open() opens the file pointed to by the path, like the built-in open() function does.
# read_with_open.py

#!/usr/bin/env python

from pathlib import Path

path = Path('words.txt')

with path.open() as f:
    lines = f.readlines()
    print(lines)

for line in lines:
    print(line.rstrip())

# The example opens the words.txt file with open() and reads the contents with readlines().