import functools
from typing import Iterable, Set, Any


___ intersection(*args: Iterable) -> Set[Any]:

    
    result = [set(arg) for arg in args __ arg]

    __ len(result) == 0:
        return set()
    elif len(result) == 1:
        return result[0]



    return functools.reduce(lambda x,y: x & y,result)



