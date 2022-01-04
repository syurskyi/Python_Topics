_______ p__

____ Previous.tail _______ tail

content = b"""Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""


# https://docs.pytest.org/en/latest/tmpdir.html#the-tmpdir-factory-fixture

@p__.fixture
___ my_file(tmp_path):
    f = tmp_path / "some_file.txt"
    f.write_bytes(content)
    r.. f


___ test_tail_various_args(my_file):
    ... tail(my_file.resolve(), 1) __ ['Become a PyBites ninja!']
    ... tail(my_file.resolve(), 2) __ ['Keep calm and code in Python!',
                                          'Become a PyBites ninja!']


___ test_tail_arg_gt_num_lines_files(my_file):
    # n of > file length basically gets the whole file, but need to do some
    # byte to str conversion and strip off last line's newline char
    actual = tail(my_file.resolve(), 10)
    expected = [line.decode("utf-8")
                ___ line __ content.splitlines()]
    ... actual __ expected