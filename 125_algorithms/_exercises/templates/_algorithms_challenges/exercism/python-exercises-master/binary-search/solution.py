___ binary_search(search_list, value
    low = 0
    high = le.(search_list) - 1
    w___ low <= high:
        middle = (low + high) // 2
        __ search_list[middle] > value:
            high = middle - 1
        ____ search_list[middle] < value:
            low = middle + 1
        ____
            r_ middle
    raise ValueError("Value not found.")
