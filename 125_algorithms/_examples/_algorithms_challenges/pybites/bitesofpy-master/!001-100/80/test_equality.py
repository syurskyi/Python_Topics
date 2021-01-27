from Previous.equality import Equality, check_equality


def test_same_reference():
    a = [1, 2, 3, 4]
    b = a
    # shallow copy (do not change original), alternatively use the copy module
    c = a[:]
    a__ check_equality(a, b) == Equality.SAME_REFERENCE
    a__ check_equality(a, c) != Equality.SAME_REFERENCE


def test_same_ordered():
    a = [1, 2, 3, 4]
    b = a[:]
    c = a
    a__ check_equality(a, b) == Equality.SAME_ORDERED
    a__ check_equality(a, c) != Equality.SAME_ORDERED  # SAME_REFERENCE


def test_same_unordered():
    a = [1, 2, 3, 4]
    b = a[::-1]
    c = b[:] + [5]
    a__ check_equality(a, b) == Equality.SAME_UNORDERED
    a__ check_equality(a, c) != Equality.SAME_UNORDERED


def test_same_unordered_deduped():
    a = [1, 2, 2, 3, 4]
    b = a[:] + [1, 3, 4, 4]
    c = b[:] + [5]
    a__ check_equality(a, b) == Equality.SAME_UNORDERED_DEDUPED
    a__ check_equality(a, c) != Equality.SAME_UNORDERED_DEDUPED


def test_not_same():
    a = [1, 2, 3]
    b = [4, 5, 6]
    a__ check_equality(a, b) == Equality.NO_EQUALITY