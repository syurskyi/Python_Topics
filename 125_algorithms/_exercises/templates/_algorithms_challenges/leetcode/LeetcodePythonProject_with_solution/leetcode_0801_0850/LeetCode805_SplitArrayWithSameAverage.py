'''
Created on Apr 24, 2018

@author: tongq
'''
class Solution(object):
    ___ splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        __ l..(arr) __ 1: r.. False
        sumA = 0
        ___ num __ arr:
            sumA += num
        arr.sort()
        ___ lenOfB __ r..(1, l..(arr)//2+1):
            __ (sumA*lenOfB)%l..(arr) __ 0:
                __ self.check(arr, (sumA*lenOfB)/l..(arr), lenOfB, 0):
                    r.. True
        r.. False
    
    ___ check(self, arr, leftSum, leftNum, startIdx):
        __ leftNum __ 0: r.. leftSum __ 0
        __ arr[startIdx] > leftSum/leftNum:
            r.. False
        ___ i __ r..(startIdx, l..(arr)-leftNum+1):
            __ i > startIdx and arr[i] __ arr[i-1]:
                continue
            __ self.check(arr, leftSum-arr[i], leftNum-1, i+1):
                r.. True
        r.. False
    
    ___ test(self):
        testCases = [
            [1,2,3,4,5,6,7,8],
            [11,1,15,2,14,16,8,9,4],
            [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = self.splitArraySameAverage(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()

