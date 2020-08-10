"""
Find the largest Python source file in a single directory.
Search Windows Python source lib, unless dir command-line arg.
"""

______ __, g__, ___
d.. _ r'C:\Python31\Lib' __ le.(___.a..) __ 1 else ___.a..[1]

allsizes _ []
allpy _ g__.g__(d.. + __.sep + '*.py')
___ filename __ allpy:
    filesize _ __.p...getsize(filename)
    allsizes.ap..((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])
