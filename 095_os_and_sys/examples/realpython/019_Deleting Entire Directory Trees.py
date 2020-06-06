# To delete non-empty directories and entire directory trees, Python offers shutil.rmtree():
#
# import shutil
#
# trash_dir = 'my_documents/bad_dir'
#
# try:
#     shutil.rmtree(trash_dir)
# except OSError as e:
#     print(f'Error: {trash_dir} : {e.strerror}')
#
# Everything in trash_dir is deleted when shutil.rmtree() is called on it. There may be cases where you want
# to delete empty folders recursively. You can do this using one of the methods discussed above in conjunction
# with os.walk():
#
# import os
#
# for dirpath, dirnames, files in os.walk('.', topdown=False):
#     try:
#         os.rmdir(dirpath)
#     except OSError as ex:
#         pass
#
# This walks down the directory tree and tries to delete each directory it finds. If the directory isn’t empty,
# an OSError is raised and that directory is skipped. The table below lists the functions covered in this section:
# Function 	Description
# os.remove() 	Deletes a file and does not delete directories
# os.unlink() 	Is identical to os.remove() and deletes a single file
# pathlib.Path.unlink() 	Deletes a file and cannot delete directories
# os.rmdir() 	Deletes an empty directory
# pathlib.Path.rmdir() 	Deletes an empty directory
# shutil.rmtree() 	Deletes entire directory tree and can be used to delete non-empty directories