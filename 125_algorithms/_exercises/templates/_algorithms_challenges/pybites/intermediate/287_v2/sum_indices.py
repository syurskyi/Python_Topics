from typing import List
from collections import defaultdict


___ sum_indices(items: List[str]) -> int:



    indexes = defaultdict(int)

    total = 0
    for i,value in enumerate(items):
        total += indexes.get(value,0)
        total += i

        indexes[value] +=  i


    return total
