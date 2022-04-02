# _______ p__
#
# ____ Previous.? _______ ?
#
# content = b"""Hello world!
# We hope that you are learning a lot of Python.
# Have fun with our Bites of Py.
# Keep calm and code in Python!
# Become a PyBites ninja!"""
#
#
# # https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-factory-fixture
#
# ?p__.f..
# ___ my_file tmp_path
#     f = ? / "some_file.txt"
#     ?.w.. ?
#     r.. f
#
#
# ___ test_tail_various_argsmy_file
#     ... ? ? 1) __  'Become a PyBites ninja!'
#     ... ? ? 2) __  'Keep calm and code in Python!',
#                                           'Become a PyBites ninja!'
#
#
# ___ test_tail_arg_gt_num_lines_files(my_file
#     # n of > file length basically gets the whole file, but need to do some
#     # byte to str conversion and strip off last line's newline char
#     actual = ? ? 10
#     expected = line.d.. utf-8
#                 ___ ? __ ?.s..
#     ... ? __ ?