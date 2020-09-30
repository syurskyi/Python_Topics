'''
Created on Apr 8, 2018

@author: tongq
'''
class Solution(object
    ___ isIdealPermutation(self, A
        """
        :type A: List[int]
        :rtype: bool
        """
        arr = A
        cmax = 0
        ___ i __ range(le.(arr)-2
            cmax = ma.(cmax, arr[i])
            __ cmax > arr[i+2]:
                r_ False
        r_ True
    
    ___ test(self
        testCases = [
            [1,0,2],
            [1,2,0],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = self.isIdealPermutation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
