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
        up, down = [0]*len(arr), [0]*len(arr)
        res = 0
        for i in range(1, len(arr)):
            __ arr[i] > arr[i-1]:
                up[i] = up[i-1]+1
        for i in range(len(arr)-1, -1, -1):
            __ arr[i] > arr[i+1]:
                down[i] = down[i+1]+1
            __ up[i] and down[i]:
                res = max(res, up[i]+down[i]+1)
        return res
    
    ___ longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        res, up, down = 0, 0, 0
        for i in range(1, len(arr)):
            __ (down and arr[i-1] < arr[i]) or (arr[i-1] == arr[i]):
                up, down = 0, 0
            __ arr[i-1] < arr[i]:
                up += 1
            elif arr[i-1] > arr[i]:
                down += 1
            __ up and down:
                res = max(res, up+down+1)
        return res
    
    ___ test(self):
        testCases = [
            [2,1,4,7,3,2,5],
            [2,2,2],
            [7,4,8],
            [1,2,3,4,3,2,1],
            [0,1,2,3,4,5,4,3,2,1,0],
            [4,3,2,1],
        ]
        for arr in testCases:
            result = self.longestMountain(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
