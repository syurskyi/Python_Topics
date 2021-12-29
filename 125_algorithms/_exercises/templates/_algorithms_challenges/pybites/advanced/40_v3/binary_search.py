from math import floor


___ binary_search(sequence, target):
    left = 0
    right = len(sequence) - 1

    while left <= right:
        mid = floor((left + right) / 2)
        val = sequence[mid]
        __ target < val:
            right = mid - 1
        elif target > val:
            left = mid + 1
        else:
            return mid
    return None
