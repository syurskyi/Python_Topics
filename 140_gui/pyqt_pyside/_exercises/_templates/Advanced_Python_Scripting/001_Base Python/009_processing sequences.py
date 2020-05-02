_____ os
_____ shutil
path = path = '/home/sergei/My_Documents/Python/Advanced Python Scripting/top_projects/render'
correctname = 'shot_01'
padding = 4

# list of files

files = os.listdir(path)
tmp = os.listdir(path)
files = []
for t in tmp:
    __ os.path.isfile(os.path.join(path, t)):
        files.append(t)

# separate

frames = []
for f in files:
    name, ext = os.path.splitext(f)
    fullName = name
    while name[-1].isdigit(
        # print(name)
        name = name[:-1]
    digits = int(fullName.replace(name, ''))
    frames.append(digits)
offset = min(frames) - 1
#print(frames)

# new name

outFolder = os.path.join(path, correctname)
__ not os.path.exists(outFolder
    os.mkdir(outFolder)
for i, f in enumerate(files
    # print(f, frames[i])
    old = os.path.join(path, f)
    name, ext = os.path.splitext(f)
    newName = correctname + '_' + st.(frames[i] - offset).zfill(padding) + ext
    new = os.path.join(path, correctname, newName)
    # print(old)
    # print(new)
    __ os.path.exists(new
        os.remove(new)
    shutil.copy(old, new)

# search missing frames

fullrange = range(min(frames), max(frames)+1)
# print(fullrange)
miss = []
for i in fullrange:
    __ not i in frames:
        miss. append(i)
# print(miss)

# message

print('Miss frames:', miss)

a = raw_input('Remove old files? [y/n]: ')
__ a __ 'y' or a __ 'Y':
    for f in files:
        os.remove(os.path.join(path, f))
print('Complete!!!')
raw_input()