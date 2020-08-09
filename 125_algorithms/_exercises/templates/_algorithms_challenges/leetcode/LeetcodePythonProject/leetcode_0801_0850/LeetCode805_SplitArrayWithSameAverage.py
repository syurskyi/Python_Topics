'''
Created on Apr 24, 2018

@author: tongq
'''
class Solution(object
    ___ splitArraySameAverage(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        __ le.(arr) __ 1: r_ False
        sumA = 0
        for num in arr:
            sumA += num
        arr.sort()
        for lenOfB in range(1, le.(arr)//2+1
            __ (sumA*lenOfB)%le.(arr) __ 0:
                __ self.check(arr, (sumA*lenOfB)/le.(arr), lenOfB, 0
                    r_ True
        r_ False
    
    ___ check(self, arr, leftSum, leftNum, startIdx
        __ leftNum __ 0: r_ leftSum __ 0
        __ arr[startIdx] > leftSum/leftNum:
            r_ False
        for i in range(startIdx, le.(arr)-leftNum+1
            __ i > startIdx and arr[i] __ arr[i-1]:
                continue
            __ self.check(arr, leftSum-arr[i], leftNum-1, i+1
                r_ True
        r_ False
    
    ___ test(self
        testCases = [
            [1,2,3,4,5,6,7,8],
            [11,1,15,2,14,16,8,9,4],
            [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.splitArraySameAverage(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

