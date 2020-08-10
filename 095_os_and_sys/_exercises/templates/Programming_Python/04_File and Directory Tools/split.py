#!/usr/bin/python
"""
################################################################################
split a file into a set of parts; join.py puts them back together;
this is a customizable version of the standard Unix split command-line
utility; because it is written in Python, it also works on Windows and
can be easily modified; because it exports a function, its logic can
also be imported and reused in other applications;
################################################################################
"""

______ ___, __
kilobytes _ 1024
megabytes _ kilobytes * 1000
chunksize _ int(1.4 * megabytes)                   # default: roughly a floppy

___ split(fromfile, todir, chunksize_chunksize):
    __ no. __.p...e..(todir):                  # caller handles errors
        __.mkdir(todir)                            # make dir, read/write parts
    ____
        ___ fname __ __.l_d_(todir):            # delete any existing files
            __.r..(__.p...j..(todir, fname))
    partnum _ 0
    input _ o..(fromfile, 'rb')                   # use binary mode on Windows
    while True:                                    # eof=empty string from read
        chunk _ input.read(chunksize)              # get next part <= chunksize
        __ no. chunk: break
        partnum +_ 1
        filename _ __.p...j..(todir, ('part%04d' % partnum))
        fileobj  _ o..(filename, 'wb')
        fileobj.w..(chunk)
        fileobj.close()                            # or simply open().write()
    input.close()
    assert partnum <_ 9999                         # join sort fails if 5 digits
    r_ partnum

__ __name__ __ '__main__':
    __ le.(___.a..) __ 2 and ___.a..[1] __ '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    ____
        __ le.(___.a..) < 3:
            interactive _ True
            fromfile _ input('File to be split? ')           # input if clicked
            todir    _ input('Directory to store part files? ')
        ____
            interactive _ False
            fromfile, todir _ ___.a..[1:3]                  # args in cmdline
            __ le.(___.a..) __ 4: chunksize _ int(___.a..[3])
        absfrom, absto _ map(__.p...a.., [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)

        ___
            parts _ split(fromfile, todir, chunksize)
        ______:
            print('Error during split:')
            print(___.exc_info()[0], ___.exc_info()[1])
        ____
            print('Split finished:', parts, 'parts are in', absto)
        __ interactive: input('Press Enter key') # pause if clicked
