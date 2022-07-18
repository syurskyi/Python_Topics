import os

print(50 * '#')
print('# ####### istdir')
print()
rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        print(d)

print()
print(50 * '#')
print('# ####### istdir')
print()

import os

def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            print(d)
            listdirs(d)


rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
listdirs(rootdir)

print()
print(50 * '#')
print('# ####### scandir')
print()
rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
for it in os.scandir(rootdir):
    if it.is_dir():
        print(it.path)


def listdirs(rootdir):
    for it in os.scandir(rootdir):
        if it.is_dir():
            print(it.path)
            listdirs(it)


rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
listdirs(rootdir)

from pathlib import Path

print()
print(50 * '#')
print('# ####### pathlib')
print()

rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
for path in Path(rootdir).iterdir():
    if path.is_dir():
        print(path)


from pathlib import Path

def listdirs(rootdir):
    for path in Path(rootdir).iterdir():
        if path.is_dir():
            print(path)
            listdirs(path)

rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
listdirs(rootdir)

print()
print(50 * '#')
print('# ####### os.walk')
print()

rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
for rootdir, dirs, files in os.walk(rootdir):
    for subdir in dirs:
        print(os.path.join(rootdir, subdir))

print()
print(50 * '#')
print('# ####### glob')
print()

import glob

rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
for path in glob.glob(f'{rootdir}/*/'):
    print(path)

import glob

rootdir = r'C:\Users\syurskyi\PycharmProjects\TD\__syurskyi_repository__\_weta\python'
for path in glob.glob(f'{rootdir}/*/**/', recursive=True):
    print(path)