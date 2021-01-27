___ insertionSort(arr):
    ___ i __ ra__(1, le.(arr)):
        key = arr[i]
        last = i - 1

        w__ last >= 0 a__ key < arr[last]:
            arr[last + 1] = arr[last]
            last = last - 1

        arr[last + 1] = key


arr = [1, 2, 3, 4, 5]
insertionSort(arr)

print(arr)