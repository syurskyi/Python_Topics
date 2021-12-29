from collections import OrderedDict

___ calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    values_sorted = dict(OrderedDict(sorted(d.items(), key=lambda t: t[0])))
    length = len(values_sorted)
    mid = (length - 1) / 2
    __ length % 2 == 0 or length == 1:
        mid_before_n = int(mid - 0.5)
        mid_before = list(values_sorted.keys())[mid_before_n]
        mid_after_n = int(mid + 0.5)
        mid_after = list(values_sorted.keys())[mid_after_n]
        return (mid_before + mid_after) / 2
    else:
        mid = int(mid)
        return list(values_sorted.keys())[mid]