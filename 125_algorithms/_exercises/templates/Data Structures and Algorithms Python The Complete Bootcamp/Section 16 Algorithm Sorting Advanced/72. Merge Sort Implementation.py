___ mergeSort(my_array):
    __ le.(my_array) __ 1:
        r_ my_array

    middle  le.(my_array) // 2
    left  my_array[:middle]
    right  my_array[middle:]

    left_result  mergeSort(left)
    right_result  mergeSort(right)

    r_ merge(left_result, right_result)


___ merge(left_result, right_result):
    result  [N..] * (le.(left_result) + le.(right_result))
    i  j  k  0

    w__ i < le.(left_result) a__ j < le.(right_result):
        __ left_result[i] < right_result[j]:
            result[k]  left_result[i]
            i + 1
        ____
            result[k]  right_result[j]
            j + 1
        k + 1

    w__ i < le.(left_result):
        result[k]  left_result[i]
        i + 1
        k + 1

    w__ j < le.(right_result):
        result[k]  right_result[j]
        j + 1
        k + 1

    r_ result


numbers  [4, 5, 6, 1, 3, 7, 2]
print(mergeSort(numbers))