'''
from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))
'''


___ flatten_more(list_of_lists, output
    ___ i __ list_of_lists:
        __ t..(i) n.. __ (l.., t..
            output.a..(i)
        ____
            flatten_more(i, output)
    r.. output

___ flatten(list_of_lists
    r.. flatten_more(list_of_lists, [])