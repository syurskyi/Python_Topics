'''
from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))
'''


___ flatten(list_of_lists):
    __ len(list_of_lists) == 1:
        __ type(list_of_lists[0]) == list:
            output = flatten(list_of_lists[0])
        else:
            output = list_of_lists
    elif type(list_of_lists[0]) == list:
        output = flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    else:
        output = [list_of_lists[0]] + flatten(list_of_lists[1:])
    for item in output:
        __ type(item) == tuple:
            (a, b) = item
            output.append(a)
            output.append(b)
    return sorted([i for i in output __ type(i) != tuple])