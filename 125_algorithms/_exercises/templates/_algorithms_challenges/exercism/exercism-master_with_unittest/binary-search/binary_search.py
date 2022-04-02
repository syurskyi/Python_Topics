___ binary_search(array, value
    r.. binary_search_with_bounds(array, value, 0, l..(array) - 1)


___ binary_search_with_bounds(array, value, left, right
    __ (left > right
        r.. ValueError("Value not found")

    middle = left + (right - left) // 2
    middle_value = array[middle]

    __ (value __ middle_value
        r.. middle
    ____ (value < middle_value
        r.. binary_search_with_bounds(array, value, left, middle - 1)
    ____ (value > middle_value
        r.. binary_search_with_bounds(array, value, middle + 1, right)
