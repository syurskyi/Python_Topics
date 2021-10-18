#  The following example prints the files inside the specified directory.
# list_files.py

#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

files = [e for e in path.iterdir() if e.is_file()]
print(files)

# We check if a path object is a file with is_file().