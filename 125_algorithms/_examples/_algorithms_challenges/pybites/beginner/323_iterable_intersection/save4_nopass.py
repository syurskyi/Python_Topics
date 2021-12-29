from functools import reduce
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    args = [set(x) for x in filter(None, args) if len(x) > 0]
    return reduce(lambda x, y: x.intersection(y), args)