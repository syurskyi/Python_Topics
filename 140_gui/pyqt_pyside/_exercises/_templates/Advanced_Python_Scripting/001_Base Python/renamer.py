_____ ___
_____ os

# print sys.argv
arg _ ___.argv[1:]

newName _ raw_input('Enter name: ')
__ newName:
    ___ i, f __ enumerate(arg
        d _ os.path.dirname(f)
        name, ext _ os.path.splitext(os.path.basename(f))
        fName _ newName + '_' + st.(i).zfill(3) + ext
        fullPath _ os.path.join(d, fName)
        # print(fullPath)
        os.rename(f, fullPath)

raw_input