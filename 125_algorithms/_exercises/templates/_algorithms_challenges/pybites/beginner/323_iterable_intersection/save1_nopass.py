from functools import reduce
from typing import Iterable, Set, Any


___ intersection(*args: Iterable) -> Set[Any]:
    args = [set(x) for x in args __ len(x) > 0]
    return list(reduce(lambda x, y: x.intersection(y), args))[0]