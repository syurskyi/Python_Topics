# A Path instance includes several methods for testing the type of file refered to by the path. This example creates several files of different types and tests those as well as a few other device-specific files available on the local operating system.
# pathlib_types.py
#
# import itertools
# import os
# import pathlib
#
# root = pathlib.Path('test_files')
#
# # Clean up from previous runs.
# if root.exists():
#     for f in root.iterdir():
#         f.unlink()
# else:
#     root.mkdir()
#
# # Create test files
# (root / 'file').write_text(
#     'This is a regular file', encoding='utf-8')
# (root / 'symlink').symlink_to('file')
# os.mkfifo(str(root / 'fifo'))
#
# # Check the file types
# to_scan = itertools.chain(
#     root.iterdir(),
#     [pathlib.Path('/dev/disk0'),
#      pathlib.Path('/dev/console')],
# )
# hfmt = '{:18s}' + ('  {:>5}' * 6)
# print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block',
#                   'Character'))
# print()
#
# fmt = '{:20s}  ' + ('{!r:>5}  ' * 6)
# for f in to_scan:
#     print(fmt.format(
#         str(f),
#         f.is_file(),
#         f.is_dir(),
#         f.is_symlink(),
#         f.is_fifo(),
#         f.is_block_device(),
#         f.is_char_device(),
#     ))
#
# Each of the methods, is_dir(), is_file(), is_symlink(), is_socket(), is_fifo(), is_block_device(), and is_char_device(), takes no arguments.
#
# $ python3 pathlib_types.py
#
# Name                 File    Dir   Link   FIFO  Block  Character
#
# test_files/fifo       False  False  False   True  False  False
# test_files/file        True  False  False  False  False  False
# test_files/symlink     True  False   True  False  False  False
# /dev/disk0            False  False  False  False   True  False
# /dev/console          False  False  False  False  False   True