_______ functools
____ typing _______ Iterable, Set, Any, cast


___ intersection(*args: Iterable) -> Set[Any]:
    cast_to_set = [set(arg) ___ arg __ args __ arg != N.. and l..(arg) != 0]

    __ l..(cast_to_set) __ 0:
        r.. set()
    
    r.. functools.reduce(set.intersection, cast_to_set)


# if __name__ == "__main__":
#     print(intersection({1,2,3}, {2,3,4}, {3,4}))
#     print(intersection([1,2,3,"1"], {1,-1}, {}))
#     print(intersection(None, "this is a string"))