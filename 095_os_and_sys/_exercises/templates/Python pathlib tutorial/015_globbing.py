#  Glob patterns specify sets of filenames with wildcard characters. For example, the *.txt represents all files with
#  names ending in .txt. The * is a wildcard standing for any string of characters. The other common wildcard is
#  the question mark (?), which stands for one character.
#
# Path provides glob() and rglob(). The latter is used for recursive globbing. It adds **/ in front of the given pattern.
# globbing.py
#
#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Documents/pyprogs')

for e in path.rglob('*.py'):
    print(e)

# for e in path.glob('**/*.py'):
#     print(e)

# The example prints all Python files in the specified directory and all its subdirectories. Notice that
# such operations may be very time consuming.
#
for e in path.rglob('*.py'):
    print(e)

# # for e in path.glob('**/*.py'):
# #     print(e)
#
# Both operations are equivalent.