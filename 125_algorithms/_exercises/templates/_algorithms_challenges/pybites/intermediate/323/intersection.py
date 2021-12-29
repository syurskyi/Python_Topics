import functools
from typing import Iterable, Set, Any, cast


___ intersection(*args: Iterable) -> Set[Any]:
    cast_to_set = [set(arg) for arg in args __ arg != None and len(arg) != 0]

    __ len(cast_to_set) == 0:
        return set()
    
    return functools.reduce(set.intersection, cast_to_set)


# if __name__ == "__main__":
#     print(intersection({1,2,3}, {2,3,4}, {3,4}))
#     print(intersection([1,2,3,"1"], {1,-1}, {}))
#     print(intersection(None, "this is a string"))