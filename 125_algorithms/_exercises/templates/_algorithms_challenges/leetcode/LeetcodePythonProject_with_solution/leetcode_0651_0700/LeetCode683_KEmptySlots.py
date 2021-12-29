'''
Created on Oct 21, 2017

@author: MT
'''
class Solution(object):
    ___ kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        __ n.. flowers: r.. -1
        n = l..(flowers)
        days = [False]*n
        ___ i __ r..(n):
            days[flowers[i]-1] = i+1
        left, right = 0, k+1
        res = float('inf')
        ___ i __ r..(n):
            __ right >= n: break
            __ days[i] __ days[right] a.. i __ right:
                res = m..(res, max(days[left], days[right]))
            __ days[i] < days[left] o. days[i] < days[right]:
                left = i
                right = k+1+i
        r.. res __ res != float('inf') ____ -1
    
    ___ test(self):
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
        ___ flowers, k __ testCases:
            print('flowers: %s' % flowers)
            print('k: %s' % k)
            result = self.kEmptySlots(flowers, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
