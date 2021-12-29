'''
from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))
'''


___ flatten(list_of_lists):
    __ l..(list_of_lists) __ 1:
        __ type(list_of_lists[0]) __ l..:
            output = flatten(list_of_lists[0])
        ____:
            output = list_of_lists
    ____ type(list_of_lists[0]) __ l..:
        output = flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    ____:
        output = [list_of_lists[0]] + flatten(list_of_lists[1:])
    r.. output