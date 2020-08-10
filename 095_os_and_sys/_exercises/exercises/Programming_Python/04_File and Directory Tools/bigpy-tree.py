"""
Find the largest Python source file in an entire directory tree.
Search the Python source lib, use pprint to display results nicely.  
"""

______ ___, __, pprint
trace _ False
__ ___.platform.startswith('win'):
    d.. _ r'C:\Python31\Lib'                 # Windows
____
    d.. _ '/usr/lib/python'                  # Unix, Linux, Cygwin

allsizes _ []
___ (thisDir, subsHere, filesHere) __ __.w..(d..):
    __ trace: print(thisDir)
    ___ filename __ filesHere:
        __ filename.e_w_('.py'):
            __ trace: print('...', filename)
            fullname _ __.p...j..(thisDir, filename)
            fullsize _ __.p...getsize(fullname)
            allsizes.ap..((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
