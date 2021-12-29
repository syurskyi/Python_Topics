from typing import List


def pascal(N: int) -> List[int]:
    """
    Return the Nth row of Pascal triangle
    """
    in_list = [1]
    out_list = []
    if N == 0:
        return out_list
    elif N == 1:
        return in_list
    else:
        for x in range(N-1):
            #print(x)
            out_list = []
            for i, v in enumerate(in_list):
                if i == 0:
                    out_list.append(v)
                else:
                    out_list.append(v + in_list[i-1])
            out_list.append(in_list[-1])
            in_list = out_list
    return out_list


print(pascal(12))