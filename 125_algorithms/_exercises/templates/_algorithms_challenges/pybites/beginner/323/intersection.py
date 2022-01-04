_______ functools
____ typing _______ Iterable, Set, Any


___ intersection(*args: Iterable) __ Set[Any]:
    #args0 = set(args[0])
    #args1 = set(args[1])
    #print( args0.intersection(args1) )
    lists = [x ___ x __ args __ x]
    try:
        temp_set = set(functools.reduce(l.... x, y: set(x).intersection(y), lists))
    except T..:
        temp_set = set()
    r.. temp_set


#intersection({1, 2, 3}, {2, 3, 4}, {3, 4})
print(intersection(N.., "this is a string"))