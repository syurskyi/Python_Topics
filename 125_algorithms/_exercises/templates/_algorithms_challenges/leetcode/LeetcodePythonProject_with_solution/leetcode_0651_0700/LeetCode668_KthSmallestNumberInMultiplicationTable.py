'''
Created on Oct 11, 2017

@author: MT
'''
c_ Solution(object):
    ___ findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        low, high = 1, m*n+1
        w.... low < high:
            mid = (low+high)//2
            c = c.. mid, m, n)
            __ c >= k:
                high = mid
            ____:
                low = mid+1
        r.. high
    
    ___ c.. self, val, m, n):
        count = 0
        ___ i __ r..(1, m+1):
            tmp = m..(val//i, n)
            count += tmp
        r.. count
    
    ___ test
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
        ___ m, n, k __ testCases:
            print('m: %s' % m)
            print('n: %s' % n)
            print('k: %s' % k)
            result = findKthNumber(m, n, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
