___ binary_search(sequence, target


    low,high 0,l..(sequence) - 1


    w.... low <_ high:
        mid (low + high)//2


        __ sequence[mid] __ target:
            r.. mid


        __ sequence[mid] < target:
            low mid + 1
        ____
            high =mid - 1


