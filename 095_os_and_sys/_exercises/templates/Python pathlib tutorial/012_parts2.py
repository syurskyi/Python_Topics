#  The following program gives other parts of a path.
# parts2.py
#
#!/usr/bin/env python

from pathlib import Path
import os

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

print(f"The stem is: {path.stem}")
print(f"The name is: {path.name}")
print(f"The suffix is: {path.suffix}")
print(f"The anchor is: {path.anchor}")

print(f"File name: {os.path.splitext(path.stem)[0]}")

print("The suffixes: ")
print(path.suffixes)

# The program prints the stem, name, suffix(es), and the anchor.
#
# $ parts2.py
# The stem is: wordpress-5.1.tar
# The name is: wordpress-5.1.tar.gz
# The suffix is: .gz
# The anchor is: C:\
# File name: wordpress-5.1
# The suffixes:
# ['.1', '.tar', '.gz']
#
# This is the output.