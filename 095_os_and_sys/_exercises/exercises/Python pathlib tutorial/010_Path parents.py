#  With parent() and parents(), we can get the logical parents of a path.
# parents.py

#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

print(f"The parent directory of {path} is {path.parent}")
print(f"The parent of the parent of {path} is {path.parent.parent}")

print(f"All the parents of {path.parent}: ")

print(list(path.parents))

# The example prints parents of a path.

print(f"The parent of the parent of {path} is {path.parent.parent}")

# We can get a parent of a parent.
#
# $ parents.py
# The parent directory of C:\Users\Jano\Documents is C:\Users\Jano
# The parent of the parent of C:\Users\Jano\Documents is C:\Users
# All the parents of C:\Users\Jano:
# [WindowsPath('C:/Users/Jano'), WindowsPath('C:/Users'), WindowsPath('C:/')]
#
# This is the output.