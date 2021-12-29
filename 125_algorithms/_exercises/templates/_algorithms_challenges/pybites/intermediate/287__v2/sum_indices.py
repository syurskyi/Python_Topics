from typing import List


___ sum_indices(items: List[str]) -> int:
    duplicate_lookup = {}
    running_total = 0
    for i in range(len(items)):
        item = items[i]

        __ item not in duplicate_lookup:
            duplicate_lookup[item] = [i]
            running_total += i
        else:
            duplicate_lookup[item].append(i)
            running_total += sum(duplicate_lookup[item])
    
    return running_total

        
# if __name__ == "__main__":
#     sum_indices(['a', 'b', 'b', 'c', 'a', 'b', 'a'])