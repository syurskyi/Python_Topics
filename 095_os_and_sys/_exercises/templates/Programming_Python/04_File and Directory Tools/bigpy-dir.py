"""
Find the largest Python source file in a single directory.
Search Windows Python source lib, unless dir command-line arg.
"""

______ __, g__, ___
dirname = r'C:\Python31\Lib' __ len(___.argv) == 1 else ___.argv[1]

allsizes = []
allpy = g__.g__(dirname + __.sep + '*.py')
___ filename __ allpy:
    filesize = __.p...getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
