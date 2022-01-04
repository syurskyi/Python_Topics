_______ p__

____ Previous.fifo _______ my_queue

q1 = my_queue(5)
q2 = my_queue(3)
q3 = my_queue(7)


@p__.mark.parametrize('fn_in,expected_result', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 2]),
    (3, [0, 1, 2, 3]),
    (4, [0, 1, 2, 3, 4]),
    (5, [1, 2, 3, 4, 5]),
    (6, [2, 3, 4, 5, 6]),
])
___ test_queue_default_arg(fn_in, expected_result):
    q1.a..(fn_in)
    ... l..(q1) __ expected_result


@p__.mark.parametrize('fn_in,expected_result', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 2]),
    (3, [1, 2, 3]),
    (4, [2, 3, 4]),
    (5, [3, 4, 5]),
    (6, [4, 5, 6]),
])
___ test_queue_less_items(fn_in, expected_result):
    q2.a..(fn_in)
    ... l..(q2) __ expected_result


@p__.mark.parametrize('fn_in,expected_result', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 2]),
    (3, [0, 1, 2, 3]),
    (4, [0, 1, 2, 3, 4]),
    (5, [0, 1, 2, 3, 4, 5]),
    (6, [0, 1, 2, 3, 4, 5, 6]),
])
___ test_queue_more_items(fn_in, expected_result):
    q3.a..(fn_in)
    ... l..(q3) __ expected_result