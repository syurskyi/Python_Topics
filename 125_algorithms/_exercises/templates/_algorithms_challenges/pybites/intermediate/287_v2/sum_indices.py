____ typing _______ List
____ collections _______ defaultdict


___ sum_indices(items: List[str]) -> int:



    indexes = defaultdict(int)

    total = 0
    ___ i,value __ enumerate(items):
        total += indexes.get(value,0)
        total += i

        indexes[value] +=  i


    r.. total
