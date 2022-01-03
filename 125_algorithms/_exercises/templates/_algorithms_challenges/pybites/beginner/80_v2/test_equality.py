____ equality _______ Equality, check_equality


___ test_same_reference():
    a = [1, 2, 3, 4]
    b = a
    # shallow copy (do not change original), alternatively use the copy module
    c = a |
    ... check_equality(a, b) __ Equality.SAME_REFERENCE
    ... check_equality(a, c) != Equality.SAME_REFERENCE


___ test_same_ordered():
    a = [1, 2, 3, 4]
    b = a |
    c = a
    ... check_equality(a, b) __ Equality.SAME_ORDERED
    ... check_equality(a, c) != Equality.SAME_ORDERED  # SAME_REFERENCE


___ test_same_unordered():
    a = [1, 2, 3, 4]
    b = a[::-1]
    c = b |  + [5]
    ... check_equality(a, b) __ Equality.SAME_UNORDERED
    ... check_equality(a, c) != Equality.SAME_UNORDERED


___ test_same_unordered_deduped():
    a = [1, 2, 2, 3, 4]
    b = a |  + [1, 3, 4, 4]
    c = b |  + [5]
    ... check_equality(a, b) __ Equality.SAME_UNORDERED_DEDUPED
    ... check_equality(a, c) != Equality.SAME_UNORDERED_DEDUPED


___ test_not_same():
    a = [1, 2, 3]
    b = [4, 5, 6]
    ... check_equality(a, b) __ Equality.NO_EQUALITY
