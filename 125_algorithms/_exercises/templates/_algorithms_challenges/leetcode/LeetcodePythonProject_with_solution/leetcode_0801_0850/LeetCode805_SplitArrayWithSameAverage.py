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
        __ len(arr) == 1: return False
        sumA = 0
        for num in arr:
            sumA += num
        arr.sort()
        for lenOfB in range(1, len(arr)//2+1):
            __ (sumA*lenOfB)%len(arr) == 0:
                __ self.check(arr, (sumA*lenOfB)/len(arr), lenOfB, 0):
                    return True
        return False
    
    ___ check(self, arr, leftSum, leftNum, startIdx):
        __ leftNum == 0: return leftSum == 0
        __ arr[startIdx] > leftSum/leftNum:
            return False
        for i in range(startIdx, len(arr)-leftNum+1):
            __ i > startIdx and arr[i] == arr[i-1]:
                continue
            __ self.check(arr, leftSum-arr[i], leftNum-1, i+1):
                return True
        return False
    
    ___ test(self):
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

__ __name__ == '__main__':
    Solution().test()

