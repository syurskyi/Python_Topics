'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object
    ___ kEmptySlots(self, flowers, k
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        __ not flowers: r_ -1
        n = le.(flowers)
        days = [False]*n
        for i in range(n
            days[flowers[i]-1] = i+1
        left, right = 0, k+1
        res = float('inf')
        for i in range(n
            __ right >= n: break
            __ days[i] __ days[right] and i __ right:
                res = min(res, max(days[left], days[right]))
            __ days[i] < days[left] or days[i] < days[right]:
                left = i
                right = k+1+i
        r_ res __ res != float('inf') else -1
    
    ___ test(self
        testCases = [
            [
                [1, 3, 2],
                1,
            ],
            [
                [1, 2, 3],
                1,
            ],
            [
                [1,2,3,4,5,6,7],
                1,
            ],
        ]
        for flowers, k in testCases:
            print('flowers: %s' % flowers)
            print('k: %s' % k)
            result = self.kEmptySlots(flowers, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
