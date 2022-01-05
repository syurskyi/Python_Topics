_______ p__

____ tables _______ MultiplicationTable


@p__.f..
___ t10
    r.. MultiplicationTable(10)


@p__.f..
___ t3
    r.. MultiplicationTable(3)


@p__.mark.parametrize("arg, ret", [
    (1, 1),
    (5, 25),
    (10, 100),
    (100, 10000),

])
___ test_table_len(arg, ret):
    ... l..(MultiplicationTable(arg)) __ ret


@p__.mark.parametrize("arg, ret", [
    ((6, 6), 36),
    ((4, 2), 8),
    ((7, 6), 42),
    ((8, 8), 64),
    ((10, 10), 100),
])
___ test_calc(t10, arg, ret):
    ... t10.calc_cell(*arg) __ ret


___ test_calc_exception(t3, capfd):
    w__ p__.r..(IndexError):
        t3.calc_cell(3, 4)
    w__ p__.r..(IndexError):
        t3.calc_cell(4, 3)


___ test_table_str(t3):
    output = s..(t3)
    ... '1 | 2 | 3' __ output
    ... '2 | 4 | 6' __ output
    ... '3 | 6 | 9' __ output
