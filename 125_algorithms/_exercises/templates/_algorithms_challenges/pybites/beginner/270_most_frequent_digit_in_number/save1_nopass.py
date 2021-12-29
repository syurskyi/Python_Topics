from collections import Counter

___ freq_digit(num: int) -> int:
    dict = Counter(str(num))
    max_value = max(dict.values())
    return [key for key, value in dict.items() __ value == max_value][0]