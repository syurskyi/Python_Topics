'''
Created on Mar 18, 2019

@author: tongq
'''
class Solution(object):
    ___ longestMountain_twoPassesONSpace(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        up, down = [0]*l..(arr), [0]*l..(arr)
        res = 0
        ___ i __ r..(1, l..(arr)):
            __ arr[i] > arr[i-1]:
                up[i] = up[i-1]+1
        ___ i __ r..(l..(arr)-1, -1, -1):
            __ arr[i] > arr[i+1]:
                down[i] = down[i+1]+1
            __ up[i] a.. down[i]:
                res = max(res, up[i]+down[i]+1)
        r.. res
    
    ___ longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        res, up, down = 0, 0, 0
        ___ i __ r..(1, l..(arr)):
            __ (down a.. arr[i-1] < arr[i]) o. (arr[i-1] __ arr[i]):
                up, down = 0, 0
            __ arr[i-1] < arr[i]:
                up += 1
            ____ arr[i-1] > arr[i]:
                down += 1
            __ up a.. down:
                res = max(res, up+down+1)
        r.. res
    
    ___ test(self):
        testCases = [
            [2,1,4,7,3,2,5],
            [2,2,2],
            [7,4,8],
            [1,2,3,4,3,2,1],
            [0,1,2,3,4,5,4,3,2,1,0],
            [4,3,2,1],
        ]
        ___ arr __ testCases:
            result = self.longestMountain(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
