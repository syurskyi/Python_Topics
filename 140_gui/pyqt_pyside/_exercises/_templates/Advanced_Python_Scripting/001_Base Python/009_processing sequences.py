_____ os
_____ shutil
path _ path _ '/home/sergei/My_Documents/Python/Advanced Python Scripting/top_projects/render'
correctname _ 'shot_01'
padding _ 4

# list of files

files _ os.listdir(path)
tmp _ os.listdir(path)
files _ []
___ t __ tmp:
    __ os.path.isfile(os.path.join(path, t)):
        files.ap..(t)

# separate

frames _ []
___ f __ files:
    name, ext _ os.path.splitext(f)
    fullName _ name
    w__ name[-1].isdigit(
        # print(name)
        name _ name[:-1]
    digits _ int(fullName.replace(name, ''))
    frames.ap..(digits)
offset _ min(frames) - 1
#print(frames)

# new name

outFolder _ os.path.join(path, correctname)
__ not os.path.exists(outFolder
    os.mkdir(outFolder)
___ i, f __ enumerate(files
    # print(f, frames[i])
    old _ os.path.join(path, f)
    name, ext _ os.path.splitext(f)
    newName _ correctname + '_' + st.(frames[i] - offset).zfill(padding) + ext
    new _ os.path.join(path, correctname, newName)
    # print(old)
    # print(new)
    __ os.path.exists(new
        os.remove(new)
    shutil.copy(old, new)

# search missing frames

fullrange _ range(min(frames), max(frames)+1)
# print(fullrange)
miss _ []
___ i __ fullrange:
    __ not i __ frames:
        miss. ap..(i)
# print(miss)

# message

print('Miss frames:', miss)

a _ raw_input('Remove old files? [y/n]: ')
__ a __ 'y' or a __ 'Y':
    ___ f __ files:
        os.remove(os.path.join(path, f))
print('Complete!!!')
raw_input