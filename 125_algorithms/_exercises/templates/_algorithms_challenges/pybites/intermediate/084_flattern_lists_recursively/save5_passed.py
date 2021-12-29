'''
from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))
'''


___ flatten_more(list_of_lists, output):
    for i in list_of_lists:
        __ type(i) not in (list, tuple):
            output.append(i)
        else:
            flatten_more(i, output)
    return output

___ flatten(list_of_lists):
    return flatten_more(list_of_lists, [])