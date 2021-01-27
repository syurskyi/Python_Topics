from math import ceil

___ find_median(arr
    n = le_(arr)
    median = find_median_util(arr, n/2+1, 0, n-1)
    print(median)


___ find_median_util(arr, k, low, high
    m = partition(arr, low, high)

    length = m - low + 1

    __ length __ k:
        r_ arr[m]

    __ length > k:
        r_ find_median_util(arr, k, low, m-1)
    ____
        r_ find_median_util(arr, k-length, m+1, high)


___ partition(arr, low, high
    pivot = get_pivot_val(arr, low, high)

    w__ low < high:
        w__ arr[low] < pivot:
            low += 1
        w__ arr[high] > pivot:
            high -= 1

        __ arr[low] __ arr[high]:
            low += 1

        # swap

        elif low < high:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp

    r_ high


___ get_pivot_val(arr, low, high

    __ high - low + 1 <= 9:
        sorted(arr)
        r_ arr[int(le_(arr)/2)]

    medians = [0] * int(ceil(( high - low +1 )/5))

    median_index = 0

    w__ high >= low:

        temp = [0]* min(5, (high - low + 1))

        ___ i __ range(0, le_(temp)):
            __ low <= high :
                temp[i] = arr[low]
                low += 1

        sorted(temp)

        medians[median_index] = temp[int(le_(temp)/2)]
        median_index += 1

    r_ get_pivot_val(medians, 0, le_(medians) - 1)


arr = [25, 24, 33, 39, 3, 18, 19, 31, 23, 49, 45, 16, 1, 29, 40, 22, 15, 20, 24, 4, 13,  34]
find_median(arr)