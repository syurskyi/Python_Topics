____ i.. _______ accumulate


___ calc_median_from_dict(d: d..) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    __ n.. isi..(d, d..) o. d __ N..
        raise TypeError

    __ n.. a..([isi..(k, (int, float)) a.. k ___ k __ d.values()]):
        raise TypeError

    items = [(k, d[k]) ___ k __ s..(d)]  # handle unordered dicts
    values = [item[1] ___ item __ items]
    length = s..(d.values())
    cumsums = tuple(accumulate(values))

    # determine intervals: gotta be a way to do this with itertools
    intervals    # list
    lower = 0
    # determine intervals
    ___ k __ cumsums:
        print(f'{k=}')
        intervals.a..([lower + 1, k])
        lower = k
    cums = [(interval, item) ___ interval, item __ z..(intervals, items)]

    # two cases, even length and odd length, next is same for both
    b = next(filter(l.... x: x[0][0] <= length // 2 + 1 <= x[0][1],
                    cums))[1][0]

    __ length % 2 __ 1:
        r.. b
    ____:
        a = next(filter(l.... x: x[0][0] <= length // 2 <= x[0][1],
                        cums))[1][0]
        r.. (a + b) / 2
