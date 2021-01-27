#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Convert One String to Another with minimum operation in Python

___ findMinOperation(s1, s2, index1, index2
    __ index1 == len(s1
        return len(s2)-index2
    __ index2 == len(s2
        return len(s1)-index1
    __ s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    ____
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min (deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrltt", 0, 0))