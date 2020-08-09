SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


___ check_lists(l1, l2
    __ l1 __ l2:
        r_ EQUAL
    __ contains(l1, l2
        r_ SUPERLIST
    __ contains(l2, l1
        r_ SUBLIST
    r_ UNEQUAL


___ contains(l1, l2
    __ not l2:
        r_ True
    __ le.(l2) > le.(l1
        r_ False
    ___ i in range(le.(l1) - le.(l2) + 1
        __ l1[i] != l2[0]:
            continue
        ___ j in range(le.(l2)):
            __ l1[i + j] != l2[j]:
                break
        ____
            r_ True
    r_ False
