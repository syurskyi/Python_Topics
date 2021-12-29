___ binary_search(sequence, target):


    low,high = 0,len(sequence) - 1


    while low <= high:
        mid = (low + high)//2


        __ sequence[mid] == target:
            return mid


        __ sequence[mid] < target:
            low = mid + 1
        else:
            high =mid - 1


