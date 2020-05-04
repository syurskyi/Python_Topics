_____ __

# print __file__
root _ __.path.d_n..(__file__)
files _ __.listdir(root)
txt _ []
___ f __ files:
    __ __.path.isfile(__.path.j..(root, f)):
        __ __.path.splitext(f)[-1] __ '.txt':
            arg.ap..(__.path.j..(root, f))

# print(arg)

newName _ raw_input('Enter name: ')
__ newName:
    ___ i, f __ enumerate(arg
        d _ __.path.d_n..(f)
        name, ext _ __.path.splitext(__.path.b..(f))
        fName _ newName + '_' + st.(i).zfill(3) + ext
        fullPath _ __.path.j..(d, fName)
        # print(fullPath)
        __.rename(f, fullPath)

raw_input