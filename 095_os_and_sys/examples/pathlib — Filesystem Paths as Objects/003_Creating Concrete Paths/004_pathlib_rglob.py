# The glob processor supports recursive scanning using the pattern prefix ** or by calling rglob() instead of glob().
# pathlib_rglob.py
#
# import pathlib
#
# p = pathlib.Path('..')
#
# for f in p.rglob('pathlib_*.py'):
#     print(f)
#
# Because this example starts from the parent directory, a recursive search is necessary to find the example files matching pathlib_*.py.
#
# $ python3 pathlib_rglob.py
#
# ../pathlib/pathlib_chmod.py
# ../pathlib/pathlib_convenience.py
# ../pathlib/pathlib_from_existing.py
# ../pathlib/pathlib_glob.py
# ../pathlib/pathlib_iterdir.py
# ../pathlib/pathlib_joinpath.py
# ../pathlib/pathlib_mkdir.py
# ../pathlib/pathlib_name.py
# ../pathlib/pathlib_operator.py
# ../pathlib/pathlib_ownership.py
# ../pathlib/pathlib_parents.py
# ../pathlib/pathlib_parts.py
# ../pathlib/pathlib_read_write.py
# ../pathlib/pathlib_resolve.py
# ../pathlib/pathlib_rglob.py
# ../pathlib/pathlib_rmdir.py
# ../pathlib/pathlib_stat.py
# ../pathlib/pathlib_symlink_to.py
# ../pathlib/pathlib_touch.py
# ../pathlib/pathlib_types.py
# ../pathlib/pathlib_unlink.py

