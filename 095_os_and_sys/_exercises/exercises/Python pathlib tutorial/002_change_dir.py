#!/usr/bin/env python

from pathlib import Path
from os import chdir

path = Path('..')

print(f'Current working directory: {path.cwd()}')

chdir(path)

print(f'Current working directory: {path.cwd()}')

chdir('..')


#  We change the current working directory. Note that the directory is changed only inside the Python program.
#
# $ change_dir.py
# Current working directory: C:\Users\Jano\Documents\pyprogs\pathlib
# Current working directory: C:\Users\Jano\Documents\pyprogs
#
# This is a sample output. 