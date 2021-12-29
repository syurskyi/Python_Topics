'''
Created on Mar 23, 2017

@author: MT
'''

class Solution(object):
    ___ isReflected(self, points):
        minVal, maxVal = float('inf'), float('-inf')
        hashmap = {}
        for point in points:
            x, y = point[0], point[1]
            minVal = min(minVal, x)
            maxVal = max(maxVal, x)
            __ y not in hashmap:
                hashmap[point[1]] = set([x])
            else:
                hashmap[point[1]].add(x)
        mid = float(minVal+maxVal)/2
        for point in points:
            x, y = point[0], point[1]
            __ x == mid:
                continue
            else:
                __ 2*mid-x not in hashmap[point[1]]:
                    return False
        return True
