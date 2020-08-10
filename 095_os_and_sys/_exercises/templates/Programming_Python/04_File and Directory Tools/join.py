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
readsize = 1024

___ j..(fromdir, tofile):
    output = o..(tofile, 'wb')
    parts  = __.l_d_(fromdir)
    parts.sort()
    ___ filename __ parts:
        filepath = __.p...j..(fromdir, filename)
        fileobj  = o..(filepath, 'rb')
        while True:
            filebytes = fileobj.read(readsize)
            __ not filebytes: break
            output.w..(filebytes)
        fileobj.close()
    output.close()

__ __name__ == '__main__':
    __ len(___.argv) == 2 and ___.argv[1] == '-help':
        print('Use: join.py [from-dir-name to-file-name]')
    ____
        __ len(___.argv) != 3:
            interactive = True
            fromdir = input('Directory containing part files? ')
            tofile  = input('Name of file to be recreated? ')
        ____
            interactive = False
            fromdir, tofile = ___.argv[1:]
        absfrom, absto = map(__.p...abspath, [fromdir, tofile])
        print('Joining', absfrom, 'to make', absto)

        try:
            j..(fromdir, tofile)
        except:
            print('Error joining files:')
            print(___.exc_info()[0], ___.exc_info()[1])
        ____
           print('Join complete: see', absto)
        __ interactive: input('Press Enter key') # pause if clicked
