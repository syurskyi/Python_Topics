'''
Created on Apr 17, 2018

@author: tongq
'''
class Solution(object
    ___ numSubarrayBoundedMax(self, A, L, R
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        arr, l, r = A, L, R
        res = 0
        j = 0
        count = 0
        for i in range(le.(arr)):
            __ l <= arr[i] <= r:
                res += i-j+1
                count = i-j+1
            ____ arr[i] < l:
                res += count
            ____
                j = i+1
                count = 0
        r_ res
    
    ___ test(self
        testCases = [
            [
                [2, 1, 4, 3],
                2, 3,
            ],
            [
                [73,55,36,5,55,14,9,7,72,52],
                32, 69,
            ],
            [
                [2,9,2,5,6],
                2, 8
            ],
        ]
        for arr, l, r in testCases:
            result = self.numSubarrayBoundedMax(arr, l, r)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
