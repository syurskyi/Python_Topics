from __future__ ______ print_function
______ __, sys

p.. = '.'

if len(sys.argv) == 2:
    p.. = sys.argv[1]

files = __.listdir(p..)
___ name __ files:
    print(name)

    full_path = __.p...j..(p.., name)
    print(full_path)

    inode = __.stat(full_path)
    print('  ' + str(inode.st_size))
    print('  ' + str(inode.st_mode))
    print('  ' + ('f' if inode.st_mode & 0100000 else '-'))
    print('  ' + ('d' if inode.st_mode & 0040000 else '-'))

    if __.p...isdir(full_path):
        print('    dir')
    elif __.p...isfile(full_path):
        print('    file')
    print('    ' + str(__.p...getsize(full_path)))
