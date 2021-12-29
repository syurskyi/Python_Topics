from typing import List


def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:
    if lst_of_lst == []:
        return lst_of_lst
    else:
        max_length = max([len(lst) for lst in lst_of_lst])
    
    for lst in lst_of_lst:
        if len(lst) == max_length:
            continue
        else:
            for i in range(max_length -len(lst)):
                lst.append(fillvalue)

    return lst_of_lst


# if __name__ == "__main__":
#     jagged_list([[1, 1, 1, 1], [0, 0, 0, 0], [1]], fillvalue=1)