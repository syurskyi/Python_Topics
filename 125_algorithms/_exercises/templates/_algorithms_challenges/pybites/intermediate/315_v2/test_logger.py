_______ logging

_______ p__

____ logger _______ sum_even_numbers


___ test_sum_numbers_function_works(caplog):
    ... sum_even_numbers([2, 9, 4, 11, 6]) __ 12


___ test_sum_numbers_logging(caplog):
    caplog.set_level(logging.INFO, logger="app")
    sum_even_numbers(l..(r..(1, 11)))
    ... l..(caplog.records) __ 1
    record = caplog.records[0]
    ... record.module __ 'logger'
    ... record.name __ 'app'
    ... record.levelname __ 'INFO'
    expected = 'Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> output: 30'
    ... record.message __ expected


___ test_sum_numbers_throws_exception(caplog):
    caplog.set_level(logging.INFO, logger="app")
    w__ p__.r.. T..
        sum_even_numbers([1, 'a', 2, 3])
    ... l..(caplog.records) __ 1
    record = caplog.records[0]
    ... record.levelname __ 'ERROR'
    expected = "Bad inputs: [1, 'a', 2, 3]"
    ... record.message __ expected
    ... record.exc_text.startswith('Traceback')
    ... record.exc_text.endswith(
        ('TypeError: not all arguments converted during '
         'string formatting'))