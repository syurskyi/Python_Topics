 # The rename() renames a file or directory.
# rename.py

#!/usr/bin/env python

from pathlib import Path
path = Path('names.txt')
path.rename('mynames.txt')

# The example renames the names.txt to mynames.txt in the current working directory.