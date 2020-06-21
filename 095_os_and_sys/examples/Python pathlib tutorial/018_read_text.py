#  The read_text() reads the contents of the file as a string. The file is opened and then closed. The optional parameters have the same meaning as in open().
# read_text.py
#
#!/usr/bin/env python

from pathlib import Path

path = Path('words.txt')

content = path.read_text()
print(content)

# The example reads the contents of the words.txt file with read_text().
#
# $ read_text.py
# blue
# forest
# sky
# ocean
# rabbit
# clue
#
# This is the output.