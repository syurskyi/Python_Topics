____ c.. _______ OrderedDict

___ calc_median_from_dict(d: d..) __ f__:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    values_sorted = d..(OrderedDict(s..(d.i.., key=l.... t: t[0])))
    length = l..(values_sorted)
    mid = (length - 1) / 2
    __ length % 2 __ 0 o. length __ 1:
        mid_before_n = i..(mid - 0.5)
        mid_before = l..(values_sorted.keys[mid_before_n]
        mid_after_n = i..(mid + 0.5)
        mid_after = l..(values_sorted.keys[mid_after_n]
        r.. (mid_before + mid_after) / 2
    ____:
        mid = i..(mid)
        r.. l..(values_sorted.keys[mid]