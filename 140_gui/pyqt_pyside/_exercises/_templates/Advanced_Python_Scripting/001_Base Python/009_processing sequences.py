_____ __
_____ shutil
path _ path _ '/home/sergei/My_Documents/Python/Advanced Python Scripting/top_projects/render'
correctname _ 'shot_01'
padding _ 4

# list of files

files _ __.listdir(path)
tmp _ __.listdir(path)
files _ []
___ t __ tmp:
    __ __.path.isfile(__.path.j..(path, t)):
        files.ap..(t)

# separate

frames _ []
___ f __ files:
    name, ext _ __.path.splitext(f)
    fullName _ name
    w__ name[-1].isdigit(
        # print(name)
        name _ name[:-1]
    digits _ int(fullName.replace(name, ''))
    frames.ap..(digits)
offset _ min(frames) - 1
#print(frames)

# new name

outFolder _ __.path.j..(path, correctname)
__ no. __.path.exists(outFolder
    __.mkdir(outFolder)
___ i, f __ enumerate(files
    # print(f, frames[i])
    old _ __.path.j..(path, f)
    name, ext _ __.path.splitext(f)
    newName _ correctname + '_' + st.(frames[i] - offset).zfill(padding) + ext
    new _ __.path.j..(path, correctname, newName)
    # print(old)
    # print(new)
    __ __.path.exists(new
        __.r..(new)
    shutil.copy(old, new)

# search missing frames

fullrange _ ra..(min(frames), max(frames)+1)
# print(fullrange)
miss _ []
___ i __ fullrange:
    __ no. i __ frames:
        miss. ap..(i)
# print(miss)

# message

print('Miss frames:', miss)

a _ raw_input('Remove old files? [y/n]: ')
__ a __ 'y' or a __ 'Y':
    ___ f __ files:
        __.r..(__.path.j..(path, f))
print('Complete!!!')
raw_input