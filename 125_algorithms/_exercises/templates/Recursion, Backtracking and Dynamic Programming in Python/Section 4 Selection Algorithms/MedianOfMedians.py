
___ median_algorithm(nums, k

    # we have to split the list into chunks of 5 items
    chunks  [nums[i:i+5] ___ i __ ra__(0, le_(nums), 5)]
    # the median is the middle item in the sorted order
    # NOTE: median of the medians is just approximately the median of the original data structure
    medians  [s..(chunk)[le_(chunk)//2] ___ chunk __ chunks]
    pivot_value  s..(medians)[le_(medians)//2]

    # PARTITION PHASE
    left_array  [n ___ n __ nums __ n < pivot_value]
    right_array  [m ___ m __ nums __ m > pivot_value]

    # selection phase
    pivot_index  le_(left_array)

    __ k < pivot_index:
        # we have to consider the left array because we are looking for
        # smaller items
        r_ median_algorithm(left_array, k)
    ____ k > pivot_index:
        # we have to consider the right array BUT we have to update k value
        # because we have created a new array
        r_ median_algorithm(right_array, k-le_(left_array)-1)
    ____
        r_ pivot_value


___ select(nums, k
    r_ median_algorithm(nums, k-1)


x  [1, -5, 0, 10, 15, 20, 3, -1, 21, 22, 23, 24, 25, 26, 27, 28, 29]
print(select(x, 1))
print(select(x, 2))
print(select(x, 3))
print(select(x, 4))
