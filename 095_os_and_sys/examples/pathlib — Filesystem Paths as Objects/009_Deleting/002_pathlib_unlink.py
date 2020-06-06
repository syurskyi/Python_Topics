# For files, symbolic links, and most other path types use unlink().
# pathlib_unlink.py
#
# import pathlib
#
# p = pathlib.Path('touched')
#
# p.touch()
#
# print('exists before removing:', p.exists())
#
# p.unlink()
#
# print('exists after removing:', p.exists())
#
# The user must have permission to remove the file, symbolic link, socket, or other file system object.
#
# $ python3 pathlib_unlink.py
#
# exists before removing: True
# exists after removing: False