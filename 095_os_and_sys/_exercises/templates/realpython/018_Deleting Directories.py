# The standard library offers the following functions for deleting directories:
#
#     os.rmdir()
#     pathlib.Path.rmdir()
#     shutil.rmtree()
#
# To delete a single directory or folder, use os.rmdir() or pathlib.rmdir(). These two functions only work if the d
# irectory you’re trying to delete is empty. If the directory isn’t empty, an OSError is raised. Here is how to delete
# a folder:

______ __

trash_dir _ 'my_documents/bad_dir'

___
    __.rmdir(trash_dir)
______ O.. __ e:
    print(f'Error: {trash_dir} : {e.strerror}')

# Here, the trash_dir directory is deleted by passing its path to os.rmdir(). If the directory isn’t empty,
# an error message is printed to the screen:
#
# Traceback (most recent call last):
#   File '<stdin>', line 1, in <module>
# OSError: [Errno 39] Directory not empty: 'my_documents/bad_dir'
#
# Alternatively, you can use pathlib to delete directories:

____ p_l_ ______ P..

trash_dir _ P..('my_documents/bad_dir')

___
    trash_dir.rmdir()
______ O.. __ e:
    print(f'Error: {trash_dir} : {e.strerror}')


# Here, you create a Path object that points to the directory to be deleted. Calling .rmdir() on the Path object
# will delete it if it is empty.