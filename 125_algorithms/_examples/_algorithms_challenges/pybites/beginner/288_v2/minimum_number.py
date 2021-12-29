from typing import List


def minimum_number(digits: List[int]) -> int:
    
    if not digits:
        return 0

    unique = set(digits)

    unique = sorted(unique)


    return int(''.join(map(str,unique)))






