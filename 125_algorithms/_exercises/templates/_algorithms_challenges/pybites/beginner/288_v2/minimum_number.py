from typing import List


___ minimum_number(digits: List[int]) -> int:
    
    __ not digits:
        return 0

    unique = set(digits)

    unique = sorted(unique)


    return int(''.join(map(str,unique)))






