_____ os

# print __file__
root = os.path.dirname(__file__)
files = os.listdir(root)
txt = []
for f in files:
    __ os.path.isfile(os.path.join(root, f)):
        __ os.path.splitext(f)[-1] __ '.txt':
            arg.append(os.path.join(root, f))

# print(arg)

newName = raw_input('Enter name: ')
__ newName:
    for i, f in enumerate(arg
        d = os.path.dirname(f)
        name, ext = os.path.splitext(os.path.basename(f))
        fName = newName + '_' + st.(i).zfill(3) + ext
        fullPath = os.path.join(d, fName)
        # print(fullPath)
        os.rename(f, fullPath)

raw_input()