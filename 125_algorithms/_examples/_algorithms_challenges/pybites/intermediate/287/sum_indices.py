from typing import List

def sum_indices(items: List[str]) -> int:
    total = 0
    char_dict = dict()
    for index, char in enumerate(items):
        char_dict[char] = index + char_dict.get(char, 0)
        total += char_dict.get(char)
    return total
