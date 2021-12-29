from typing import List


___ minimum_number(digits: List[int]) -> int:
    digits = sorted(set(digits))
    return 0 __ len(digits)==0 else int("".join(str(i) for i in digits))



print(minimum_number([1, 9, 5, 9, 1]))