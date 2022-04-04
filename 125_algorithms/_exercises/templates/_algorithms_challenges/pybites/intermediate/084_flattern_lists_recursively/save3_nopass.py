'''
from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))
'''


___ flatten(list_of_lists
    __ l..(list_of_lists) __ 1:
        __ t..(list_of_lists[0]) __ l..:
            output = flatten(list_of_lists[0])
        ____
            output = list_of_lists
    ____ t..(list_of_lists[0]) __ l..:
        output = flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    ____
        output = [list_of_lists[0]] + flatten(list_of_lists[1:])
    ___ item __ output:
        __ t..(item) __ t..:
            (a, b) = item
            output.a..(a)
            output.a..(b)
    r.. s..([i ___ i __ output __ t..(i) != t..])