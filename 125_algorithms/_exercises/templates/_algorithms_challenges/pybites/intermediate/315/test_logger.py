_______ l___

_______ p__

____ logger _______ sum_even_numbers


___ test_sum_numbers_function_works(caplog
    ... sum_even_numbers([2, 9, 4, 11, 6]) __ 12


___ test_sum_numbers_logging(caplog
    caplog.s.. l___.INFO, logger="app")
    sum_even_numbers(l..(r..(1, 11)))
    ... l.. c__.r.. __ 1
    record = caplog.records[0]
    ... record.module __ 'logger'
    ...  r__n.. __ 'app'
    ...  r__l.. __ 'INFO'
    e.. = 'Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> output: 30'
    ...  r__m.. __ e..


___ test_sum_numbers_throws_exception(caplog
    caplog.s.. l___.INFO, logger="app")
    w__ p__.r.. T..
        sum_even_numbers([1, 'a', 2, 3])
    ... l.. c__.r.. __ 1
    record = caplog.records[0]
    ...  r__l.. __ 'ERROR'
    e.. = "Bad inputs: [1, 'a', 2, 3]"
    ...  r__m.. __ e..
    ... record.exc_text.s.. 'Traceback')
    ... record.exc_text.e..
        ('TypeError: not all arguments converted during '
         'string formatting'