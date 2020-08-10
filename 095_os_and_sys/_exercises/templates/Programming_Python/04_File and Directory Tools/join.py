#!/usr/bin/python
"""
################################################################################
join all part files in a dir created by split.py, to re-create file.
This is roughly like a 'cat fromdir/* > tofile' command on unix, but is
more portable and configurable, and exports the join operation as a
reusable function.  Relies on sort order of filenames: must be same
length.  Could extend split/join to pop up Tkinter file selectors.
################################################################################
"""

______ __, ___
readsize _ 1024

___ j..(fromdir, tofile):
    output _ o..(tofile, 'wb')
    parts  _ __.l_d_(fromdir)
    parts.sort()
    ___ filename __ parts:
        filepath _ __.p...j..(fromdir, filename)
        fileobj  _ o..(filepath, 'rb')
        while True:
            filebytes _ fileobj.read(readsize)
            __ no. filebytes: break
            output.w..(filebytes)
        fileobj.close()
    output.close()

__ __name__ __ '__main__':
    __ le.(___.a..) __ 2 and ___.a..[1] __ '-help':
        print('Use: join.py [from-dir-name to-file-name]')
    ____
        __ le.(___.a..) !_ 3:
            interactive _ True
            fromdir _ input('Directory containing part files? ')
            tofile  _ input('Name of file to be recreated? ')
        ____
            interactive _ False
            fromdir, tofile _ ___.a..[1:]
        absfrom, absto _ map(__.p...abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)

        ___
            j..(fromdir, tofile)
        ______:
            print('Error joining files:')
            print(___.exc_info()[0], ___.exc_info()[1])
        ____
           print('Join complete: see', absto)
        __ interactive: input('Press Enter key') # pause if clicked
