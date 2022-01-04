____ functools _______ reduce
____ typing _______ Iterable, Set, Any


___ intersection(*args: Iterable) __ Set[Any]:
    args = [set(x) ___ x __ args __ l..(x) > 0]
    r.. l..(reduce(l.... x, y: x.intersection(y), args))[0]