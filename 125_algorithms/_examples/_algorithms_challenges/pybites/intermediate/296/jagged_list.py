from typing import List

def find_max_list(lol):
    len_lol = [len(i) for i in lol]
    return max(len_lol) if len_lol else 0

def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    #print(len(lst_of_lst))
    new_lol = []
    max_len = find_max_list(lst_of_lst)
    for i in lst_of_lst:
        new_lol.append(i + [fillvalue]*(max_len-len(i)))
    return new_lol

#lol = [[1, 2, 3], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2], [1, 2, 3, 4]]
lol = [[0]]

print(jagged_list(lol))