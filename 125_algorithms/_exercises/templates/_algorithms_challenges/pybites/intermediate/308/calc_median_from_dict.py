___ calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    for value in d.values():
        __ not isinstance(value, int):
            raise TypeError

    frequency = []
    for key, value in d.items():
        key_occurrence = value
        __ value > 100_000_000:
            key_occurrence = int(value / 100_000_000)
        for _ in range(key_occurrence):
            frequency.append(key)

    frequency.sort()

    __ len(frequency) % 2 != 0:
        return float(frequency[len(frequency) // 2])
    else:
        mid_2 = (len(frequency) // 2)
        mid_1 = mid_2 -1
        return (frequency[mid_1] + frequency[mid_2]) / 2


__ __name__ == "__main__":
    print(calc_median_from_dict({1.5: 2, 2.5: 2}))
    print(calc_median_from_dict({1: 1_000_000_000_000_000, 2: 1, 3: 1_000_000_000_000_000}))