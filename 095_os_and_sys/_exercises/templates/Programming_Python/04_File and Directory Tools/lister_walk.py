"list file tree with os.walk"

______ sys, os

def lister(root):                                           # for a root dir
    ___ (thisdir, subshere, fileshere) __ os.walk(root):    # generate dirs in tree
        print('[' + thisdir + ']')
        ___ fname __ fileshere:                             # print files in this dir
            path = os.path.join(thisdir, fname)             # add dir name prefix
            print(path)

if __name__ == '__main__':
    lister(sys.argv[1])                                     # dir name in cmdline
