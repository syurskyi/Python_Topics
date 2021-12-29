from typing import List
import itertools

def minimum_number(digits: List[int]) -> int:
    list = []
    for i in range(len(digits)):
        if len(digits) == 1:
            list.append(digits)
        if digits == 0:
            list.append(o)
        for set in itertools.permutations(digits, r=None):
            list.append("".join(filter(str.isdigit, str(set))))
    new_list = list[1:]
    for i in range(0, len(new_list)):
        new_list[i] = int(new_list[i])
    smallest = new_list[0]
    for i in range(1, len(new_list)):
        if smallest > new_list[i]:
            smallest = new_list[i]
    return smallest