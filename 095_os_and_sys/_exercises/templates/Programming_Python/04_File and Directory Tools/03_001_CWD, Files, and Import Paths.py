# C:\...\PP4E\System> type whereami.py
import os, sys
print('my os.getcwd =>', os.getcwd()) # show my cwd execution dir
print('my sys.path =>', sys.path[:6]) # show first 6 import paths
# input() # wait for keypress if clicked

# C:\...\PP4E\System> set PYTHONPATH=C:\PP4thEd\Examples
# C:\...\PP4E\System> python whereami.py
# my os.getcwd => C:\...\PP4E\System
# my sys.path => ['C:\\...\\PP4E\\System', 'C:\\PP4thEd\\Examples', ...more... ]

# C:\...\PP4E> python System\whereami.py
# my os.getcwd => C:\...\PP4E
# my sys.path => ['C:\\...\\PP4E\\System', 'C:\\PP4thEd\\Examples', ...more... ]
# C:\...\PP4E> cd System\temp
# C:\...\PP4E\System\temp> python ..\whereami.py
# my os.getcwd => C:\...\PP4E\System\temp
# my sys.path => ['C:\\...\\PP4E\\System', 'C:\\PP4thEd\\Examples', ...]
#
# my os.getcwd => C:\...\PP4E\System
# my sys.path => ['C:\\...\\PP4E\\System', ...more... ]