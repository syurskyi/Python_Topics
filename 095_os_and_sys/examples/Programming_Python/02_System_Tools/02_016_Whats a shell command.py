# C:\...\PP4E\System> dir /B ...type a shell command line
# helloshell.py ...its output shows up here
# more.py ...DOS is the shell on Windows
# more.pyc
# spam.txt
# __init__.py
# C:\...\PP4E\System> type helloshell.py
# a Python program
# print('The Meaning of Life')

# C:\...\PP4E\System> python
import os
os.system('dir /B')
# names files in the folder

print('#' * 52)
os.system('type helloshell.py')
# a Python program
# print('The Meaning of Life')
# 0
# ######################################################################################################################

os.system('type hellshell.py')
# The system cannot find the file specified.
# 1
# ######################################################################################################################