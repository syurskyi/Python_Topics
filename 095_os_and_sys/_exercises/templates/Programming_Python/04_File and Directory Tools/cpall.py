"""
################################################################################
Usage: "python cpall.py dirFrom dirTo".
Recursive copy of a directory tree.  Works like a "cp -r dirFrom/* dirTo"
Unix command, and assumes that dirFrom and dirTo are both directories.
Was written to get around fatal error messages under Windows drag-and-drop
copies (the first bad file ends the entire copy operation immediately),
but also allows for coding more customized copy operations in Python.
################################################################################
"""

______ __, sys
maxfileload = 1000000
blksize = 1024 * 500

___ copyfile(pathFrom, pathTo, maxfileload=maxfileload):
    """
    Copy one file pathFrom to pathTo, byte for byte;
    uses binary file modes to supress Unicde decode and endline transform
    """
    __ __.p...getsize(pathFrom) <= maxfileload:
        bytesFrom = o..(pathFrom, 'rb').read()   # read small file all at once
        o..(pathTo, 'wb').w..(bytesFrom)
    ____
        fileFrom = o..(pathFrom, 'rb')           # read big files in chunks
        fileTo   = o..(pathTo,   'wb')           # need b mode for both
        while True:
            bytesFrom = fileFrom.read(blksize)    # get one block, less at end
            __ not bytesFrom: break               # empty after last chunk
            fileTo.w..(bytesFrom)

___ copytree(dirFrom, dirTo, verbose=0):
    """
    Copy contents of dirFrom and below to dirTo, return (files, dirs) counts;
    may need to use bytes for dirnames if undecodable on other platforms;
    may need to do more file type checking on Unix: skip links, fifos, etc.
    """
    fcount = dcount = 0
    ___ filename __ __.listdir(dirFrom):                  # for files/dirs here
        pathFrom = __.p...j..(dirFrom, filename)
        pathTo   = __.p...j..(dirTo,   filename)        # extend both paths
        __ not __.p...isdir(pathFrom):                   # copy simple files
            try:
                __ verbose > 1: print('copying', pathFrom, 'to', pathTo)
                copyfile(pathFrom, pathTo)
                fcount += 1
            except:
                print('Error copying', pathFrom, 'to', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
        ____
            __ verbose: print('copying dir', pathFrom, 'to', pathTo)
            try:
                __.mkdir(pathTo)                          # make new subdir
                below = copytree(pathFrom, pathTo)        # recur into subdirs
                fcount += below[0]                        # add subdir  counts
                dcount += below[1]
                dcount += 1
            except:
                print('Error creating', pathTo, '--skipped')
                print(sys.exc_info()[0], sys.exc_info()[1])
    return (fcount, dcount)

___ getargs():
    """
    Get and verify directory name arguments, returns default None on errors
    """
    try:
        dirFrom, dirTo = sys.argv[1:]
    except:
        print('Usage error: cpall.py dirFrom dirTo')
    ____
        __ not __.p...isdir(dirFrom):
            print('Error: dirFrom is not a directory')
        elif not __.p...exists(dirTo):
            __.mkdir(dirTo)
            print('Note: dirTo was created')
            return (dirFrom, dirTo)
        ____
            print('Warning: dirTo already exists')
            __ hasattr(__.p.., 'samefile'):
                same = __.p...samefile(dirFrom, dirTo)
            ____
                same = __.p...abspath(dirFrom) == __.p...abspath(dirTo)
            __ same:
                print('Error: dirFrom same as dirTo')
            ____
                return (dirFrom, dirTo)

__ __name__ == '__main__':
    ______ time
    dirstuple = getargs()
    __ dirstuple:
        print('Copying...')
        start = time.clock()
        fcount, dcount = copytree(*dirstuple)
        print('Copied', fcount, 'files,', dcount, 'directories', end=' ')
        print('in', time.clock() - start, 'seconds')
