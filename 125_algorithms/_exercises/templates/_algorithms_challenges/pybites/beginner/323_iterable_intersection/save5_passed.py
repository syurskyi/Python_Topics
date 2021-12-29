from functools import reduce
from typing import Iterable, Set, Any


___ intersection(*args: Iterable) -> Set[Any]:
    args = [set(x) for x in filter(None, args) __ len(x) > 0]
    __ args == []:
        return set()
    return reduce(lambda x, y: x.intersection(y), args)