___ two_sums(numbers: l.., target: i..
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    num_list = s..(e..(numbers), key=l.... x: x[1])
    ___ x __ r..(l..(numbers:
        i, n = num_list[x]
        ___ j, m __ num_list[x + 1:]:
            n_m = n + m
            __ n_m __ target:
                r.. (i, j)
            __ n_m > target:
                _____
    r.. N..
