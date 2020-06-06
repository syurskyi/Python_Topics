# There are three methods for accessing the directory listings to discover the names of files available on the file system. iterdir() is a generator, yielding a new Path instance for each item in the containing directory.
# pathlib_iterdir.py
#
# import pathlib
#
# p = pathlib.Path('.')
#
# for f in p.iterdir():
#     print(f)
#
# If the Path does not refer to a directory, iterdir() raises NotADirectoryError.
#
# $ python3 pathlib_iterdir.py
#
# example_link
# index.rst
# pathlib_chmod.py
# pathlib_convenience.py
# pathlib_from_existing.py
# pathlib_glob.py
# pathlib_iterdir.py
# pathlib_joinpath.py
# pathlib_mkdir.py
# pathlib_name.py
# pathlib_operator.py
# pathlib_ownership.py
# pathlib_parents.py
# pathlib_parts.py
# pathlib_read_write.py
# pathlib_resolve.py
# pathlib_rglob.py
# pathlib_rmdir.py
# pathlib_stat.py
# pathlib_symlink_to.py
# pathlib_touch.py
# pathlib_types.py
# pathlib_unlink.py