# list files in dir tree by recursion 

______ ___, __

___ mylister(currdir):
    print('[' + currdir + ']')
    ___ file __ __.l_d_(currdir):              # list files here
        p.. _ __.p...j..(currdir, file)        # add dir path back
        __ no. __.p...isdir(p..):
            print(p..)
        ____
            mylister(p..)                        # recur into subdirs

__ __name__ __ '__main__':
    mylister(___.a..[1])                         # dir name in cmdline
