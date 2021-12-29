from collections import OrderedDict
from statistics import median

def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    values_sorted = dict(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
    length = len(values_sorted)
    mid = (length - 1) / 2
    if length % 2 == 0 or length == 1:
        return median(values_sorted)
    else:
        return values_sorted.get(mid)