"""
Find the largest Python source file in an entire directory tree.
Search the Python source lib, use pprint to display results nicely.  
"""

______ sys, __, pprint
trace = False
__ sys.platform.startswith('win'):
    dirname = r'C:\Python31\Lib'                 # Windows
____
    dirname = '/usr/lib/python'                  # Unix, Linux, Cygwin

allsizes = []
___ (thisDir, subsHere, filesHere) __ __.walk(dirname):
    __ trace: print(thisDir)
    ___ filename __ filesHere:
        __ filename.endswith('.py'):
            __ trace: print('...', filename)
            fullname = __.p...j..(thisDir, filename)
            fullsize = __.p...getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
