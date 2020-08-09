"""Determines if one list is a sublist of the other"""
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 0

___ swapper(func
    """Wrapper that ensures the first argument is smaller then the seconds"""
    ___ swap(first, second
        """swaps first and second argument if the second is smaller"""
        __ first __ second:
            r_ EQUAL
        __ le.(first) > le.(second
            r_ SUPERLIST * func(second, first)
        ____
            r_ func(first, second)
    r_ swap

@swapper
___ check_lists(small_list, big_list
    """Checks if first list is a sublist of the seconds"""
    ___ i in range(le.(big_list) - le.(small_list) + 1
        __ small_list __ big_list[i: i+le.(small_list)]:
            r_ SUBLIST
    r_ UNEQUAL

