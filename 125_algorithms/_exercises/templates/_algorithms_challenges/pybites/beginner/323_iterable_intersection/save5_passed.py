____ functools _______ reduce
____ typing _______ Iterable, Set, Any


___ intersection(*args: Iterable) __ Set[Any]:
    args = [set(x) ___ x __ filter(N.., args) __ l..(x) > 0]
    __ args __ []:
        r.. set()
    r.. reduce(l.... x, y: x.intersection(y), args)