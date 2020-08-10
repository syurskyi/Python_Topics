"""
Find the largest Python source file in an entire directory tree.
Search the Python source lib, use pprint to display results nicely.  
"""

______ sys, __, pprint
trace = False
if sys.platform.startswith('win'):
    dirname = r'C:\Python31\Lib'                 # Windows
else:
    dirname = '/usr/lib/python'                  # Unix, Linux, Cygwin

allsizes = []
___ (thisDir, subsHere, filesHere) __ __.walk(dirname):
    if trace: print(thisDir)
    ___ filename __ filesHere:
        if filename.endswith('.py'):
            if trace: print('...', filename)
            fullname = __.path.join(thisDir, filename)
            fullsize = __.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
