"list file tree with os.walk"

______ sys, __

___ lister(root):                                           # for a root dir
    ___ (thisdir, subshere, fileshere) __ __.walk(root):    # generate dirs in tree
        print('[' + thisdir + ']')
        ___ fname __ fileshere:                             # print files in this dir
            p.. = __.p...j..(thisdir, fname)             # add dir name prefix
            print(p..)

__ __name__ == '__main__':
    lister(sys.argv[1])                                     # dir name in cmdline
