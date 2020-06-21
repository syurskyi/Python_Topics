#  We refer to files with their absolute file paths or relative paths. The paths have different representations; Windows uses different file paths than Linux.
# path_names.py
#
#!/usr/bin/env python

from pathlib import Path

path = Path('C:/Users/Jano/Downloads/wordpress-5.1.tar.gz')

print(path)
print(path.as_uri())
print(path.as_posix())

# The example shows three different file path structures.
#
# $ path_names.py
# C:\Users\Jano\Downloads\wordpress-5.1.tar.gz
# file:///C:/Users/Jano/Downloads/wordpress-5.1.tar.gz
# C:/Users/Jano/Downloads/wordpress-5.1.tar.gz
#
# The first one is the Windows file path. The second one is an URI style. The third one is the POSIX style.