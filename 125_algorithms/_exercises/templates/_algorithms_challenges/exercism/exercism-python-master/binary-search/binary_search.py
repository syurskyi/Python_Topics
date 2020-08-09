___ binary_search(list_of_numbers, number
    start, end = 0, le.(list_of_numbers) - 1
    w___ start <= end:
        middle = (start + end) // 2
        __ number > list_of_numbers[middle]:
            start = middle + 1
        ____ number < list_of_numbers[middle]:
            end = middle - 1
        ____
            r_ middle
    raise ValueError("{} not in list".format(number))
