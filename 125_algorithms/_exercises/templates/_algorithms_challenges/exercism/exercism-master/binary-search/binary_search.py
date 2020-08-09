___ binary_search(array, value
    r_ binary_search_with_bounds(array, value, 0, le.(array) - 1)


___ binary_search_with_bounds(array, value, left, right
    __ (left > right
        raise ValueError("Value not found")

    middle = left + (right - left) // 2
    middle_value = array[middle]

    __ (value __ middle_value
        r_ middle
    ____ (value < middle_value
        r_ binary_search_with_bounds(array, value, left, middle - 1)
    ____ (value > middle_value
        r_ binary_search_with_bounds(array, value, middle + 1, right)
