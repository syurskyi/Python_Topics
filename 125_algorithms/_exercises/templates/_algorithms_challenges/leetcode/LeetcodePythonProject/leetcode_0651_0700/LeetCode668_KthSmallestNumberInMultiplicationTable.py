'''
Created on Oct 11, 2017

@author: MT
'''
class Solution(object
    ___ findKthNumber(self, m, n, k
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low, high = 1, m*n+1
        w___ low < high:
            mid = (low+high)//2
            c = self.count(mid, m, n)
            __ c >= k:
                high = mid
            ____
                low = mid+1
        r_ high
    
    ___ count(self, val, m, n
        count = 0
        for i in range(1, m+1
            tmp = min(val//i, n)
            count += tmp
        r_ count
    
    ___ test(self
        testCases = [
            [
                3,
                3,
                5,
            ],
            [
                2,
                3,
                6,
            ],
        ]
        for m, n, k in testCases:
            print('m: %s' % m)
            print('n: %s' % n)
            print('k: %s' % k)
            result = self.findKthNumber(m, n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
