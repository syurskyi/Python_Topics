from typing import List


___ jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:

    
    __ not lst_of_lst:
        return lst_of_lst
    max_length = max(len(l) for l in lst_of_lst)


    for l in lst_of_lst:
        l.extend([fillvalue] * (max_length - len(l)))


    return lst_of_lst





