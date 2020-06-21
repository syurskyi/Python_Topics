#  Path consists of subelements, such as drive or root.
# parts.py
#
#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents')

print(path.parts)
print(path.drive)
print(path.root)

# The program prints some parts of a path.

print(path.parts)

# The parts gives access to the path’s various components.

print(path.drive)

# The drive gives a string representing the drive letter or name, if any.

print(path.root)

# The root gives a string representing the (local or global) root, if any.

# $ parts.py
# ('C:\\', 'Users', 'Jano', 'Documents')
# C:
# \
#
# This is the output.
# The following program gives other parts of a path.