"""
Find the largest Python source file in an entire directory tree.
Search the Python source lib, use pprint to display results nicely.  
"""

______ ___, __, pprint
trace _ False
__ ___.platform.startswith('win'):
    dirname _ r'C:\Python31\Lib'                 # Windows
____
    dirname _ '/usr/lib/python'                  # Unix, Linux, Cygwin

allsizes _ []
___ (thisDir, subsHere, filesHere) __ __.walk(dirname):
    __ trace: print(thisDir)
    ___ filename __ filesHere:
        __ filename.endswith('.py'):
            __ trace: print('...', filename)
            fullname _ __.p...j..(thisDir, filename)
            fullsize _ __.p...getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
