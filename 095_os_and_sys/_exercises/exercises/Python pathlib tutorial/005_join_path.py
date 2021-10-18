#!/usr/bin/env python

from pathlib import Path

path = Path.home()

docs = path / 'Documents'
pictures = path / 'Pictures'

print(docs)
print(pictures)

#  In the example, we join two paths with /.
#
# $ join_path.py
# C:\Users\Jano\Documents
# C:\Users\Jano\Pictures
#
# This is the output. 