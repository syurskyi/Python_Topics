'''
Created on Jun 10, 2019

@author: tongq
'''
class Solution(object):
    ___ maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = i = 0
        ___ j __ r..(l..(seats)):
            __ seats[j] __ 1:
                __ i __ 0:
                    res = j
                ____:
                    res = max(res, (j-i+1) >> 1)
                i = j+1
        r.. max(res, l..(seats)-i)
    
    ___ maxDistToClosest_twoPass(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # two passes, there is a better solution for one pass
        n = l..(seats)
        left = [0]*(n+1)
        right = [0]*(n+1)
        left[0] = float('inf')
        ___ i __ r..(n):
            __ seats[i] __ 0:
                left[i+1] = left[i]+1
        right[-1] = float('inf')
        ___ i __ r..(n-1, -1, -1):
            __ seats[i] __ 0:
                right[i] = right[i+1]+1
        res = float('-inf')
        ___ i __ r..(n):
            __ left[i+1] != 0 a.. right[i] != 0:
                res = max(res, m..(left[i+1], right[i]))
        r.. res
    
    ___ test(self):
        testCases = [
            [1,0,0,0,1,0,1],
            [1,0,0,0],
            [0,1],
            [1,0],
        ]
        ___ seats __ testCases:
            result = self.maxDistToClosest(seats)
            print('result: %s' % result)
            print('-='*30)

__ __name__ __ '__main__':
    Solution().test()
