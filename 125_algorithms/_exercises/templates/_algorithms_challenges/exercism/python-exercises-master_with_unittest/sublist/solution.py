SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


___ check_lists(l1, l2):
    __ l1 == l2:
        return EQUAL
    __ contains(l1, l2):
        return SUPERLIST
    __ contains(l2, l1):
        return SUBLIST
    return UNEQUAL


___ contains(l1, l2):
    __ not l2:
        return True
    __ len(l2) > len(l1):
        return False
    for i in range(len(l1) - len(l2) + 1):
        __ l1[i] != l2[0]:
            continue
        for j in range(len(l2)):
            __ l1[i + j] != l2[j]:
                break
        else:
            return True
    return False
