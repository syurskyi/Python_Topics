 # The write_text opens the file in text mode, writes data to it, and closes the file.
# write_text.py

#!/usr/bin/python3

from pathlib import Path

path = Path('myfile.txt')
path.touch()

path.write_text('This is myfile.txt')

# The example creates a new empty file with touch() and writes some text data into the file with write_text().