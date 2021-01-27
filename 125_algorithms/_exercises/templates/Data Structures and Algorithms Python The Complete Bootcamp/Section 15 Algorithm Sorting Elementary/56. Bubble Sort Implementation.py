___ bubbleSort(arr):
    ___ iter __ range(le.(arr)):
        ___ index __ range(0, le.(arr) - 1 - iter):
            __ arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]


arr = [29, 10, 14, 37, 14]
bubbleSort(arr)

print(arr)