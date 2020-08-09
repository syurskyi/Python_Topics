'''
Created on Apr 4, 2018

@author: tongq
'''
class Solution(object
    ___ maxChunksToSorted(self, arr
        """
        :type arr: List[int]
        :rtype: int
        """
        n = le.(arr)
        maxOfLeft = [0]*n
        minOfRight = [0]*n
        maxOfLeft[0] = arr[0]
        ___ i in range(1, n
            maxOfLeft[i] = max(maxOfLeft[i-1], arr[i])
        minOfRight[-1] = arr[-1]
        ___ i in range(n-2, -1, -1
            minOfRight[i] = min(minOfRight[i+1], arr[i])
        res = 0
        ___ i in range(n-1
            __ maxOfLeft[i] <= minOfRight[i+1]:
                res += 1
        r_ res+1
    
    ___ test(self
        testCases = [
            [4,3,2,1,0],
            [1,0,2,3,4],
            [0,2,1,4,3],
        ]
        ___ arr in testCases:
            print('arr: %s' % arr)
            result = self.maxChunksToSorted(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
