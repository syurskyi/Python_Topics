___ calc_median_from_dict(d: d..) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """


    keys = s..(d.keys())

    total_values = s..(d.values())

    odd = F..
    __ total_values % 2 __ 0:
        median_count = total_values//2
    ____:
        odd = T..
        median_count = total_values//2 + 1



    median = total_values//2


    s = 0

    ___ i,key __ e..(keys):
        s += d[key]
        __ s >= median_count:
            __ odd:
                r.. key
            r.. key __ s > median_count ____ (key + keys[i +1])/2

    

    











