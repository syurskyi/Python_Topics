_____ os

# print __file__
root _ os.path.dirname(__file__)
files _ os.listdir(root)
txt _ []
___ f __ files:
    __ os.path.isfile(os.path.join(root, f)):
        __ os.path.splitext(f)[-1] __ '.txt':
            arg.ap..(os.path.join(root, f))

# print(arg)

newName _ raw_input('Enter name: ')
__ newName:
    ___ i, f __ enumerate(arg
        d _ os.path.dirname(f)
        name, ext _ os.path.splitext(os.path.basename(f))
        fName _ newName + '_' + st.(i).zfill(3) + ext
        fullPath _ os.path.join(d, fName)
        # print(fullPath)
        os.rename(f, fullPath)

raw_input()