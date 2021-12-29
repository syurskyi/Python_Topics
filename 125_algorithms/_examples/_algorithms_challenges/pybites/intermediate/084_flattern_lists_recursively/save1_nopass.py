from iteration_utilities import deepflatten

def flatten(list_of_lists):
    return list(deepflatten(list_of_lists))