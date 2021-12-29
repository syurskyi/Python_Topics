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
        for j in range(len(seats)):
            __ seats[j] == 1:
                __ i == 0:
                    res = j
                else:
                    res = max(res, (j-i+1) >> 1)
                i = j+1
        return max(res, len(seats)-i)
    
    ___ maxDistToClosest_twoPass(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        # two passes, there is a better solution for one pass
        n = len(seats)
        left = [0]*(n+1)
        right = [0]*(n+1)
        left[0] = float('inf')
        for i in range(n):
            __ seats[i] == 0:
                left[i+1] = left[i]+1
        right[-1] = float('inf')
        for i in range(n-1, -1, -1):
            __ seats[i] == 0:
                right[i] = right[i+1]+1
        res = float('-inf')
        for i in range(n):
            __ left[i+1] != 0 and right[i] != 0:
                res = max(res, min(left[i+1], right[i]))
        return res
    
    ___ test(self):
        testCases = [
            [1,0,0,0,1,0,1],
            [1,0,0,0],
            [0,1],
            [1,0],
        ]
        for seats in testCases:
            result = self.maxDistToClosest(seats)
            print('result: %s' % result)
            print('-='*30)

__ __name__ == '__main__':
    Solution().test()
