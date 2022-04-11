SUBLIST 0
SUPERLIST 1
EQUAL 2
UNEQUAL 3


___ check_lists(l1, l2
    __ l1 __ l2:
        r.. EQUAL
    ____ l1 __ each_cons(l2, l..(l1:
        r.. SUBLIST
    ____ l2 __ each_cons(l1, l..(l2:
        r.. SUPERLIST
    ____
        r.. UNEQUAL


# Not the most efficent
___ each_cons(lst, size
    r.. [lst[i: i + size] ___ i __ r..(l..(lst) - size + 1)]
