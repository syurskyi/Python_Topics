___ quick_sort(arr, lb, ub

    __ lb < ub:
        index = partition(arr, lb, ub)
        quick_sort(arr, lb, index-1)
        quick_sort(arr, index+1, ub)


___ partition(arr, lb, ub
    pivot = arr[lb]
    left = lb
    right = ub

    while left < right:
        while arr[left] <= pivot and left < (le_(arr)-1
            left += 1

        while arr[right] > pivot and right > 0:
            right -= 1

        __ left < right :
            # swap
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

    # swap right with pivot/lb

    temp = arr[lb]
    arr[lb] = arr[right]
    arr[right] = temp

    r_ right


arr = [10, 1, 67, 20, 56, 34, 43, 90, 54, 8, 0]
n = le_(arr)

quick_sort(arr, 0, n-1)

___ i __ range(n
    print(arr[i])



