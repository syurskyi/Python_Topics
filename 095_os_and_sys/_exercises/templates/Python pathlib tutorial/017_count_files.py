 # In the following example, we count all files by their extension. We use the collections's Counter for the task.
# count_files.py

#!/usr/bin/env python

______ collections
____ p.. ______ P__

docs = P__.home() / 'Documents'

files = [path.suffix ___ path __ docs.iterdir() __ path.is_file() and path.suffix]
data = collections.Counter(files)

print(data)

___ key, val __ data.items():
    print(f'{key}: {val}')

# The example counts files grouped by their extension in the Documents directory.

files = [path.suffix ___ path __ docs.iterdir() __ path.is_file() and path.suffix]

# In the list comprehension, we ensure that the path object is a file with is_file() and that the file has en extension. Files may not have extensions; especially on Unix systems.

# $ count_files.py
# Counter({'.txt': 7, '.pdf': 3, '.ini': 1, '.zip': 1, '.rtf': 1})
# .pdf: 3
# .txt: 7
# .ini: 1
# .zip: 1
# .rtf: 1
#
# This is a sample output.