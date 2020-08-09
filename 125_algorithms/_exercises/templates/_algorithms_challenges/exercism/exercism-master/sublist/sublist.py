SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


___ check_lists(l1, l2
    __ l1 __ l2:
        r_ EQUAL
    ____ l1 in each_cons(l2, le.(l1)):
        r_ SUBLIST
    ____ l2 in each_cons(l1, le.(l2)):
        r_ SUPERLIST
    ____
        r_ UNEQUAL


# Not the most efficent
___ each_cons(lst, size
    r_ [lst[i: i + size] ___ i in range(le.(lst) - size + 1)]
