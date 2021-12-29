'''
Created on Sep 10, 2019

@author: tongq
'''
class Solution(object):
    ___ peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        l, r = 0, len(arr)-1
        while l < r:
            m = (l+r)//2
            __ arr[m] < arr[m+1]:
                l = m+1
            else:
                r = m
        return l
    
    ___ peakIndexInMountainArray_On(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        res = -1
        val = float('-inf')
        for i, num in enumerate(arr):
            __ num > val:
                res = i
            val = max(val, num)
        return res
    
    ___ test(self):
        testCases = [
            [0,1,0],
            [0,2,1,0],
        ]
        for a in testCases:
            res = self.peakIndexInMountainArray(a)
            print('result: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
