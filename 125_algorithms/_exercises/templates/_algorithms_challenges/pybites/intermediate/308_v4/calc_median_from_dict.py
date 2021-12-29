from itertools import accumulate


___ calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    __ not isinstance(d, dict) or d is None:
        raise TypeError

    __ not all([isinstance(k, (int, float)) and k for k in d.values()]):
        raise TypeError

    items = [(k, d[k]) for k in sorted(d)]  # handle unordered dicts
    values = [item[1] for item in items]
    length = sum(d.values())
    cumsums = tuple(accumulate(values))

    # determine intervals: gotta be a way to do this with itertools
    intervals = []
    lower = 0
    # determine intervals
    for k in cumsums:
        print(f'{k=}')
        intervals.append([lower + 1, k])
        lower = k
    cums = [(interval, item) for interval, item in zip(intervals, items)]

    # two cases, even length and odd length, next is same for both
    b = next(filter(lambda x: x[0][0] <= length // 2 + 1 <= x[0][1],
                    cums))[1][0]

    __ length % 2 == 1:
        return b
    else:
        a = next(filter(lambda x: x[0][0] <= length // 2 <= x[0][1],
                        cums))[1][0]
        return (a + b) / 2
