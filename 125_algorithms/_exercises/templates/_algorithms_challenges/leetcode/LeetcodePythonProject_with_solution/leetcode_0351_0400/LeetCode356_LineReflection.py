'''
Created on Mar 23, 2017

@author: MT
'''

c_ Solution(o..):
    ___ isReflected  points):
        minVal, maxVal = float('inf'), float('-inf')
        hashmap    # dict
        ___ point __ points:
            x, y = point[0], point[1]
            minVal = m..(minVal, x)
            maxVal = m..(maxVal, x)
            __ y n.. __ hashmap:
                hashmap[point[1]] = set([x])
            ____:
                hashmap[point[1]].add(x)
        mid = float(minVal+maxVal)/2
        ___ point __ points:
            x, y = point[0], point[1]
            __ x __ mid:
                _____
            ____:
                __ 2*mid-x n.. __ hashmap[point[1]]:
                    r.. F..
        r.. T..
