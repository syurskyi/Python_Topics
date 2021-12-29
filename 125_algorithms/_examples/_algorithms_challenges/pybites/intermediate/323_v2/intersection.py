from functools import reduce
from typing import Iterable, Set, Any


def intersection(*args: Iterable) -> Set[Any]:
    args = [set(arg) for arg in args if arg and arg != '']
    return reduce(set.intersection, args) if args else set()
