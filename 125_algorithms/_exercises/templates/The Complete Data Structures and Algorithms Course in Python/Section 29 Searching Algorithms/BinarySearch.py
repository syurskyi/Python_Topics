#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Searching algorithms - Binary Search
_____ math
___ binarySearch(array, value
    start = 0
    end = le_(array)-1
    middle = math.floor((start+end)/2)
    w__ no.(array[middle]__value) a__ start<=end:
        __ value < array[middle]:
            end = middle - 1
        ____
            start = middle + 1 
        middle = math.floor((start+end)/2)
        # print(start, middle, end)
    __ array[middle] __ value:
        r_ middle
    ____
        r_ -1
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))
# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME