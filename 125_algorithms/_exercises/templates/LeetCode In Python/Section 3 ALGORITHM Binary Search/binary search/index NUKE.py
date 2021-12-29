
_______ math


___ binarySearch(arr, target):
    left  0
    right  l..(arr)-1
    w___ left < right:

        mid  math.floor(left + (right - left)/2)
        # Check if x is present at mid
        __ arr[mid] __ target:
            r.. mid

        # If x is greater, ignore left half
        ____ arr[mid] < target:
            left  mid + 1

        # If x is smaller, ignore right half
        ____:
            right  mid - 1

    # If we reach here, then the element was not present
    r.. -1


arr  [1, 2, 3, 4, 5, 6]
target  6

result  binarySearch(arr, target)

__ result ! -1:
    print("Element is present at index %d" % result)
____:
    print("Element is not present in array")
