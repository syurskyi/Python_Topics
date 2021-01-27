#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# productOfArray Solution

___ productOfArray(arr
    __ len(arr) == 0:
        return 1
    return arr[0] * productOfArray(arr[1:])

print(productOfArray([1,2,3])) #6
print(productOfArray([1,2,3,10])) #60

