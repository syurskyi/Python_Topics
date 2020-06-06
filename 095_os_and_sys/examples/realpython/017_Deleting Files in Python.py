# To delete a single file, use pathlib.Path.unlink(), os.remove(). or os.unlink().
# os.remove() and os.unlink() are semantically identical. To delete a file using os.remove(), do the following:
#
# import os
#
# data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
# os.remove(data_file)
#
# Deleting a file using os.unlink() is similar to how you do it using os.remove():
#
# import os
#
# data_file = 'C:\\Users\\vuyisile\\Desktop\\Test\\data.txt'
# os.unlink(data_file)
#
# Calling .unlink() or .remove() on a file deletes the file from the filesystem. These two functions will throw
# an OSError if the path passed to them points to a directory instead of a file. To avoid this, you can either check
# that what you’re trying to delete is actually a file and only delete it if it is, or you can use exception handling
# to handle the OSError:
#
# import os
#
# data_file = 'home/data.txt'
#
# # If the file exists, delete it
# if os.path.isfile(data_file):
#     os.remove(data_file)
# else:
#     print(f'Error: {data_file} not a valid filename')
#
# os.path.isfile() checks whether data_file is actually a file. If it is, it is deleted by the call to os.remove().
# If data_file points to a folder, an error message is printed to the console.
# The following example shows how to use exception handling to handle errors when deleting files:
#
# import os
#
# data_file = 'home/data.txt'
#
# # Use exception handling
# try:
#     os.remove(data_file)
# except OSError as e:
#     print(f'Error: {data_file} : {e.strerror}')
#
# The code above attempts to delete the file first before checking its type. If data_file isn’t actually a file,
# the OSError that is thrown is handled in the except clause, and an error message is printed to the console.
# The error message that gets printed out is formatted using Python f-strings.
#
# Finally, you can also use pathlib.Path.unlink() to delete files:
#
# from pathlib import Path
#
# data_file = Path('home/data.txt')
#
# try:
#     data_file.unlink()
# except IsADirectoryError as e:
#     print(f'Error: {data_file} : {e.strerror}')
#
# This creates a Path object called data_file that points to a file. Calling .remove() on data_file will
# delete home/data.txt. If data_file points to a directory, an IsADirectoryError is raised. It is worth noting that
# the Python program above has the same permissions as the user running it. If the user does not have permission
# to delete the file, a PermissionError is raised.