'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object):
    ___ numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        count = [0]*121
        ___ x __ ages:
            count[x] += 1
        res = 0
        ___ i __ r..(1, 121):
            __ i > 14:
                res += count[i]*(count[i]-1+count[i-1]-count[i//2+7])
            count[i] += count[i-1]
        r.. res
    
    ___ test(self):
        testCases = [
            [16,16],
            [16,17,18],
            [20,30,100,110,120],
            [54,23,102,90,40,74,112,74,76,21],
        ]
        ___ ages __ testCases:
            print('ages: %s' % ages)
            result = self.numFriendRequests(ages)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
