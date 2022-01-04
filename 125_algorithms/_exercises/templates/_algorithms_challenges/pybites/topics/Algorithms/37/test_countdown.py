_______ i___

____ countdown _______ countdown_for, countdown_recursive

expected = '''10
9
8
7
6
5
4
3
2
1
time is up
'''
expected_other_start_arg = '''13
12
11
'''
expected_other_start_arg += expected


___ test_countdown_for(capfd):
    countdown_for()
    out, _ = capfd.readouterr()
    ... out __ expected


___ test_countdown_recursive(capfd):
    countdown_recursive()
    out, _ = capfd.readouterr()
    ... out __ expected


___ test_test_countdown_recursive_different_start(capfd):
    countdown_recursive(13)
    out, _ = capfd.readouterr()
    ... out __ expected_other_start_arg


___ test_recursion_used
    func = countdown_recursive
    err = f'expecting {func.__name__} twice in your answer'
    ... i___.getsource(func).c.. func.__name__) __ 2, err