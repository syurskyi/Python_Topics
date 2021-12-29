___ calc_median_from_dict(d: d..) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    ___ value __ d.values():
        __ n.. isi..(value, int):
            raise TypeError

    frequency    # list
    ___ key, value __ d.items():
        key_occurrence = value
        __ value > 100_000_000:
            key_occurrence = int(value / 100_000_000)
        ___ _ __ r..(key_occurrence):
            frequency.a..(key)

    frequency.sort()

    __ l..(frequency) % 2 != 0:
        r.. float(frequency[l..(frequency) // 2])
    ____:
        mid_2 = (l..(frequency) // 2)
        mid_1 = mid_2 -1
        r.. (frequency[mid_1] + frequency[mid_2]) / 2


__ __name__ __ "__main__":
    print(calc_median_from_dict({1.5: 2, 2.5: 2}))
    print(calc_median_from_dict({1: 1_000_000_000_000_000, 2: 1, 3: 1_000_000_000_000_000}))