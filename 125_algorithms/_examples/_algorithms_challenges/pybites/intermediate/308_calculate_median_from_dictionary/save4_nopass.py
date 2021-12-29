from collections import OrderedDict

def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """

    values_sorted = dict(OrderedDict(sorted(d.items(), key=lambda t: t[0])))

    if len(values_sorted) == 1:
        return list(values_sorted.keys())[0]

    number = sum(values_sorted.values())
    determinate = number / 2
    i = 0
    i2 = 0
    the_key = []

    for key, value in values_sorted.items():
        if i < determinate:
            i += value
        else:
            the_key.append(key)
            i2 += value

    the_key_true = the_key[0]
    before = [key for key in values_sorted.keys() if key < the_key_true][-1]

    if i == i2:
        return (before + the_key_true) / 2
    else:
        return before