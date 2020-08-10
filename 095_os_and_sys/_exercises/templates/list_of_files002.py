from __future__ ______ print_function
______ __, ___

p.. _ '.'

__ len(___.argv) == 2:
    p.. _ ___.argv[1]

files _ __.l_d_(p..)
___ name __ files:
    print(name)

    full_path _ __.p...j..(p.., name)
    print(full_path)

    inode _ __.stat(full_path)
    print('  ' + str(inode.st_size))
    print('  ' + str(inode.st_mode))
    print('  ' + ('f' __ inode.st_mode & 0100000 else '-'))
    print('  ' + ('d' __ inode.st_mode & 0040000 else '-'))

    __ __.p...isdir(full_path):
        print('    dir')
    elif __.p...isfile(full_path):
        print('    file')
    print('    ' + str(__.p...getsize(full_path)))
