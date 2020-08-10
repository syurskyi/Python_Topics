from __future__ ______ print_function
______ __, sys

path = '.'

if len(sys.argv) == 2:
    path = sys.argv[1]

files = __.listdir(path)
___ name __ files:
    print(name)

    full_path = __.path.join(path, name)
    print(full_path)

    inode = __.stat(full_path)
    print('  ' + str(inode.st_size))
    print('  ' + str(inode.st_mode))
    print('  ' + ('f' if inode.st_mode & 0100000 else '-'))
    print('  ' + ('d' if inode.st_mode & 0040000 else '-'))

    if __.path.isdir(full_path):
        print('    dir')
    elif __.path.isfile(full_path):
        print('    file')
    print('    ' + str(__.path.getsize(full_path)))
