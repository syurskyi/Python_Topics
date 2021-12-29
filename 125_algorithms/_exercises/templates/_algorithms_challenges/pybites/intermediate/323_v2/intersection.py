from functools import reduce
from typing import Iterable, Set, Any


___ intersection(*args: Iterable) -> Set[Any]:
    args = [set(arg) for arg in args __ arg and arg != '']
    return reduce(set.intersection, args) __ args else set()
