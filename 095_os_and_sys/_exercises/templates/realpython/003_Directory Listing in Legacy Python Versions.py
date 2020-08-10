# # In versions of Python prior to Python 3, os.listdir() is the method to use to get a directory listing:
#
# ______ __
# entries _ __.l_d_ my_directory/'
#
# # os.listdir() returns a Python list containing the names of the files and subdirectories in the directory given
# # by the path argument:
#
# __.l_d_('my_directory/')
# # ['sub_dir_c', 'file1.py', 'sub_dir_b', 'file3.txt', 'file2.csv', 'sub_dir']
#
# # A directory listing like that isn’t easy to read. Printing out the output of a call to os.listdir() using
# # a loop helps clean things up:
#
# entries _ __.l_d_ 'my_directory/'
# ___ entry __ ?
#     print ?
#
#
# # sub_dir_c
# # file1.py
# # sub_dir_b
# # file3.txt
# # file2.csv
# # sub_dir
