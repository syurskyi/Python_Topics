# To list subdirectories instead of files, use one of the methods below. Here’s how to use os.listdir() and os.path():
#
______ os

# List all subdirectories using os.listdir
basepath = 'my_directory/'
___ entry __ os.listdir(basepath):
    if os.path.isdir(os.path.join(basepath, entry)):
        print(entry)

print()
print()
#
# Manipulating filesystem paths this way can quickly become cumbersome when you have multiple calls to os.path.join().
# Running this on my computer produces the following output:
#
# sub_dir_c
# sub_dir_b
# sub_dir
#
# Here’s how to use os.scandir():

______ os

# List all subdirectories using scandir()
basepath = 'my_directory/'
with os.scandir(basepath) as entries:
    ___ entry __ entries:
        if entry.is_dir():
            print(entry.name)

print()
print()

# As in the file listing example, here you call .is_dir() on each entry returned by os.scandir(). If the entry is
# a directory, .is_dir() returns True, and the directory’s name is printed out. The output is the same as above:
#
# sub_dir_c
# sub_dir_b
# sub_dir
#
# Here’s how to use pathlib.Path():

from pathlib ______ Path

# List all subdirectory using pathlib
basepath = Path('my_directory/')
___ entry __ basepath.iterdir():
    if entry.is_dir():
        print(entry.name)

# Calling .is_dir() on each entry of the basepath iterator checks if an entry is a file or a directory.
# If the entry is a directory, its name is printed out to the screen, and the output produced is the same as
# the one from the previous example:
#
# sub_dir_c
# sub_dir_b
# sub_dir

