'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object):
    ___ isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        cmax = 0
        for i in range(len(arr)-2):
            cmax = max(cmax, arr[i])
            __ cmax > arr[i+2]:
                return False
        return True
    
    ___ test(self):
        testCases = [
            [1,0,2],
            [1,2,0],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.isIdealPermutation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
