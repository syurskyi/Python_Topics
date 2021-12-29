#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Convert One String to Another with minimum operation in Python

___ findMinOperation(s1, s2, index1, index2
    __ index1 __ le_(s1
        r_ le_(s2)-index2
    __ index2 __ le_(s2
        r_ le_(s1)-index1
    __ s1[index1] __ s2[index2]:
        r_ findMinOperation(s1, s2, index1+1, index2+1)
    ____
        deleteOp  1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp  1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp  1 + findMinOperation(s1, s2, index1+1, index2+1)
        r_ min (deleteOp, insertOp, replaceOp)

print(findMinOperation("table", "tbrltt", 0, 0))