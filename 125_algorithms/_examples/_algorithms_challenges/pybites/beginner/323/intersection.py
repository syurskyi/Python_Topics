import functools
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    #args0 = set(args[0])
    #args1 = set(args[1])
    #print( args0.intersection(args1) )
    lists = [x for x in args if x]
    try:
        temp_set = set(functools.reduce(lambda x, y: set(x).intersection(y), lists))
    except TypeError:
        temp_set = set()
    return temp_set


#intersection({1, 2, 3}, {2, 3, 4}, {3, 4})
print(intersection(None, "this is a string"))