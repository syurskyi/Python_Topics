____ i.. _______ i..

_______ p__

____ Previous.traffic _______ traffic_light, State


?p__.f.. s.._"module"
___ slice1
    it traffic_light()
    r.. l..(islice(it, 96


?p__.f.. s.._"module"
___ slice2
    it traffic_light()
    r.. l..(islice(it, 100, 217


___ test_iterator_islice(slice1, slice2
    ... l..(slice1) __ 96
    ... l..(slice2) __ 117

    ... slice1[0] __ State(color='red', command='Stop', timeout=2)
    ... slice2[0] __ State(color='green', command='Go', timeout=2)

    ... slice1[-1] __ State(color='amber', command='Caution', timeout=0.5)
    ... slice2[-1] __ State(color='red', command='Stop', timeout=2)


___ test_equal_values_in_islice(slice1
    ___ color __ 'red green amber'.s.. :
        ... s..(1 ___ state __ slice1 __ state.color __ color) __ 32


___ test_return_types(slice2
    ... a..(t..(state) __ State ___ state __ slice2)


?p__.m__.p. "color, expected", [
    ('red', 64),
    ('green', 64),
    ('amber', 16),
])
___ test_timings(slice1, color, e..
    timeout_for_color s..(state.timeout ___ state __ slice1
                            __ state.color __ color)
    ... timeout_for_color __ e..