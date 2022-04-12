____ c.. _______ OrderedDict
____ s.. _______ median

___ calc_median_from_dict(d: d..) __ f__:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    values_sorted d..(OrderedDict(s..(d.i.., k.._l.... t: t[0])))
    length l..(values_sorted)
    mid (length - 1) / 2
    __ length % 2 __ 0 o. length __ 1:
        r.. median(values_sorted)
    ____
        r.. values_sorted.g.. mid)