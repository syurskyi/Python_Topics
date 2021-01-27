#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# someRecursive Solution

___ someRecursive(arr, cb
    __ len(arr) == 0:
        return False
    __ not(cb(arr[0])):
        return someRecursive(arr[1:], cb)
    return True

___ isOdd(num
    __ num%2==0:
        return False
    ____
        return True


print(someRecursive([1,2,3,4], isOdd)) # true
print(someRecursive([4,6,8,9], isOdd)) # true
print(someRecursive([4,6,8], isOdd)) # false
