'''
Created on Mar 23, 2017

@author: MT
'''

c_ Solution(object):
    ___ isReflected(self, points):
        minVal, maxVal = float('inf'), float('-inf')
        hashmap    # dict
        ___ point __ points:
            x, y = point[0], point[1]
            minVal = m..(minVal, x)
            maxVal = max(maxVal, x)
            __ y n.. __ hashmap:
                hashmap[point[1]] = set([x])
            ____:
                hashmap[point[1]].add(x)
        mid = float(minVal+maxVal)/2
        ___ point __ points:
            x, y = point[0], point[1]
            __ x __ mid:
                continue
            ____:
                __ 2*mid-x n.. __ hashmap[point[1]]:
                    r.. F..
        r.. T..
