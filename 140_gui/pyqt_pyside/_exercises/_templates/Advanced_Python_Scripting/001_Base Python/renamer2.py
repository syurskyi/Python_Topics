import os

# print __file__
root = os.path.dirname(__file__)
files = os.listdir(root)
txt = []
for f in files:
    if os.path.isfile(os.path.join(root, f)):
        if os.path.splitext(f)[-1] == '.txt':
            arg.append(os.path.join(root, f))

# print(arg)

newName = raw_input('Enter name: ')
if newName:
    for i, f in enumerate(arg):
        d = os.path.dirname(f)
        name, ext = os.path.splitext(os.path.basename(f))
        fName = newName + '_' + str(i).zfill(3) + ext
        fullPath = os.path.join(d, fName)
        # print(fullPath)
        os.rename(f, fullPath)

raw_input()