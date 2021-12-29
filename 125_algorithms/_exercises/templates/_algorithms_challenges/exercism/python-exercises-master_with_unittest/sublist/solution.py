SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


___ check_lists(l1, l2):
    __ l1 __ l2:
        r.. EQUAL
    __ contains(l1, l2):
        r.. SUPERLIST
    __ contains(l2, l1):
        r.. SUBLIST
    r.. UNEQUAL


___ contains(l1, l2):
    __ n.. l2:
        r.. True
    __ l..(l2) > l..(l1):
        r.. False
    ___ i __ r..(l..(l1) - l..(l2) + 1):
        __ l1[i] != l2[0]:
            continue
        ___ j __ r..(l..(l2)):
            __ l1[i + j] != l2[j]:
                break
        ____:
            r.. True
    r.. False
