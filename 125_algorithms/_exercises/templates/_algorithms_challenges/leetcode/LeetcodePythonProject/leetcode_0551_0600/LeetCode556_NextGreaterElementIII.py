'''
Created on Aug 27, 2017

@author: MT
'''
class Solution(object
    ___ nextGreaterElement(self, n
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        arr = list(s)
        i = le.(s)-1
        w___ i > 0 and arr[i-1] >= arr[i]:
            i -= 1
        __ i __ 0:
            r_ -1
        j = le.(s)-1
        ind = i
        w___ i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        j = ind
        w___ j < le.(s) and arr[j] <= arr[ind-1]:
            j += 1
        arr[ind-1], arr[j] = arr[j], arr[ind-1]
        res = int(''.join(arr))
        __ res >= 1 << 32-1:
            r_ -1
        r_ res
    
    ___ test(self
        testCases = [
            21,
            123,
            4112,
            12000,
        ]
        for n in testCases:
            print('n: %s' % n)
            result = self.nextGreaterElement(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
