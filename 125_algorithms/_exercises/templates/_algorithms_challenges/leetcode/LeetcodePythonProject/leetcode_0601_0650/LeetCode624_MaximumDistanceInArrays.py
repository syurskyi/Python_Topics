'''
Created on Sep 10, 2017

@author: MT
'''

class Solution(object
    ___ maxDistance(self, arrays
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        __ not arrays:
            r_ 0
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        maxDis = 0
        ___ i in range(1, le.(arrays)):
            arr = arrays[i]
            maxDis = max(maxDis, abs(arr[-1]-minVal))
            maxDis = max(maxDis, abs(maxVal-arr[0]))
            minVal = min(minVal, arr[0])
            maxVal = max(maxVal, arr[-1])
        r_ maxDis
    
    ___ test(self
        testCases = [
            [
                [1,2,3],
                [4,5],
                [1,2,3]
            ],
        ]
        ___ arrays in testCases:
            print('arrays: %s' % arrays)
            result = self.maxDistance(arrays)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
