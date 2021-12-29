def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """


    keys = sorted(d.keys())

    total_values = sum(d.values())

    odd = False
    if total_values % 2 == 0:
        median_count = total_values//2
    else:
        odd = True
        median_count = total_values//2 + 1



    median = total_values//2


    s = 0

    for i,key in enumerate(keys):
        s += d[key]
        if s >= median_count:
            if odd:
                return key
            return key if s > median_count else (key + keys[i +1])/2

    

    











