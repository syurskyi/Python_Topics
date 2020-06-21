# In versions of Python prior to Python 3, os.listdir() is the method to use to get a directory listing:

import os
entries = os.listdir('my_directory/')

# os.listdir() returns a Python list containing the names of the files and subdirectories in the directory given
# by the path argument:

os.listdir('my_directory/')
# ['sub_dir_c', 'file1.py', 'sub_dir_b', 'file3.txt', 'file2.csv', 'sub_dir']

# A directory listing like that isn’t easy to read. Printing out the output of a call to os.listdir() using
# a loop helps clean things up:

entries = os.listdir('my_directory/')
for entry in entries:
    print(entry)


# sub_dir_c
# file1.py
# sub_dir_b
# file3.txt
# file2.csv
# sub_dir
