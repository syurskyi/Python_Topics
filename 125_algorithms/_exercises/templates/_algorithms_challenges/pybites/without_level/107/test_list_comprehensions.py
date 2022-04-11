____ list_comprehensions _______ filter_positive_even_numbers


___ test_filter_positive_and_negatives
    numbers l..(r..(-10, 11
    ... filter_positive_even_numbers(numbers) __ [2, 4, 6, 8, 10]


___ test_only_positives
    numbers [2, 4, 51, 44, 47, 10]
    ... filter_positive_even_numbers(numbers) __ [2, 4, 44, 10]


___ test_filter_zero_and_negatives
    numbers [0, -1, -3, -5]
    ... filter_positive_even_numbers(numbers) __ []