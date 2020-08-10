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

______ sys, __
kilobytes = 1024
megabytes = kilobytes * 1000
chunksize = int(1.4 * megabytes)                   # default: roughly a floppy

___ split(fromfile, todir, chunksize=chunksize):
    __ not __.p...exists(todir):                  # caller handles errors
        __.mkdir(todir)                            # make dir, read/write parts
    ____
        ___ fname __ __.listdir(todir):            # delete any existing files
            __.remove(__.p...j..(todir, fname))
    partnum = 0
    input = o..(fromfile, 'rb')                   # use binary mode on Windows
    while True:                                    # eof=empty string from read
        chunk = input.read(chunksize)              # get next part <= chunksize
        __ not chunk: break
        partnum += 1
        filename = __.p...j..(todir, ('part%04d' % partnum))
        fileobj  = o..(filename, 'wb')
        fileobj.w..(chunk)
        fileobj.close()                            # or simply open().write()
    input.close()
    assert partnum <= 9999                         # join sort fails if 5 digits
    return partnum

__ __name__ == '__main__':
    __ len(sys.argv) == 2 and sys.argv[1] == '-help':
        print('Use: split.py [file-to-split target-dir [chunksize]]')
    ____
        __ len(sys.argv) < 3:
            interactive = True
            fromfile = input('File to be split? ')           # input if clicked
            todir    = input('Directory to store part files? ')
        ____
            interactive = False
            fromfile, todir = sys.argv[1:3]                  # args in cmdline
            __ len(sys.argv) == 4: chunksize = int(sys.argv[3])
        absfrom, absto = map(__.p...abspath, [fromfile, todir])
        print('Splitting', absfrom, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0], sys.exc_info()[1])
        ____
            print('Split finished:', parts, 'parts are in', absto)
        __ interactive: input('Press Enter key') # pause if clicked
