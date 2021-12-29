'''
from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))
'''


def flatten_more(list_of_lists, output):
    for i in list_of_lists:
        if type(i) not in (type([]), type(())):
            output.append(i)
        else:
            flatten_more(i, output)
    return output

def flatten(list_of_lists):
    return flatten_more(list_of_lists, [])