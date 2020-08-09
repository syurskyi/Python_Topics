'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object
    ___ bestRotation(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        n = le.(arr)
        change = [1]*n
        for i in range(n
            change[(i-arr[i]+1)%n] -= 1
        for i in range(1, n
            change[i] += change[i-1]
        r_ change.index(max(change))
    
    # This EASY solution is TLE    
    ___ bestRotation_slow(self, A
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        idx, maxVal = 0, float('-inf')
        for i in range(le.(arr)):
            val = self.getScore(arr, i)
            __ val > maxVal:
                maxVal = val
                idx = i
        r_ idx
    
    ___ getScore(self, arr, k
        res = 0
        arr0 = arr[k:]+arr[:k]
        for i, num in enumerate(arr0
            __ num <= i: res += 1
        r_ res
    
    ___ test(self
        testCases = [
            [2, 3, 1, 4, 0],
            [1, 3, 0, 2, 4],
        ]
        for arr in testCases:
            print('arr: %s' % arr)
            result = self.bestRotation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
