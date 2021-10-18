#  The iterdir() yields path objects of the directory contents.
# list_dirs.py

#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

dirs = [e for e in path.iterdir() if e.is_dir()]
print(dirs)

# The example prints the subdirectories of the specified directory.
# We check if the path object is a directory with is_dir().