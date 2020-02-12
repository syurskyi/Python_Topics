import sys
import os

# print sys.argv
arg = sys.argv[1:]

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