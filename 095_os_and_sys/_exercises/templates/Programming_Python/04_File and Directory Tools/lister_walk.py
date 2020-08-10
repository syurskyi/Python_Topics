"list file tree with os.walk"

______ ___, __

___ lister(root):                                           # for a root dir
    ___ (thisdir, subshere, fileshere) __ __.w..(root):    # generate dirs in tree
        print('[' + thisdir + ']')
        ___ fname __ fileshere:                             # print files in this dir
            p.. _ __.p...j..(thisdir, fname)             # add dir name prefix
            print(p..)

__ __name__ __ '__main__':
    lister(___.a..[1])                                     # dir name in cmdline
