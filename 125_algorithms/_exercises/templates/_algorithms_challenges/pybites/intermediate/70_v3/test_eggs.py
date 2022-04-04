_______ p__

____ eggs _______ EggCreator, COLORS


___ test_iterator_type
    eg = EggCreator(10)
    ... t..(eg) __ EggCreator


___ test_len_iterator_is_limit_input_arg
    ec = EggCreator(2)
    ... l..(l..(ec __ 2
    ec = EggCreator(5)
    ... l..(l..(ec __ 5


___ test_call_next_on_iterator
    ec = EggCreator(2)
    next_egg = next(ec)
    ... next_egg.s.. [0] __ COLORS


___ test_iterator_raises_stop_iteration_exception
    ec = EggCreator(2)
    next(ec)
    next(ec)
    w__ p__.r..(StopIteration
        next(ec)


___ test_iterator_generates_random_colors
    ec = EggCreator(20)
    output1 = l..(ec)
    ec = EggCreator(20)
    output2 = l..(ec)
    ... output1 != output2