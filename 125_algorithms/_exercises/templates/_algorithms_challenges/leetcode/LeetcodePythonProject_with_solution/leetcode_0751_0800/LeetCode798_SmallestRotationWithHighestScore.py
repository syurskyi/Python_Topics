'''
Created on Apr 18, 2018

@author: tongq
'''
class Solution(object):
    ___ bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        n = l..(arr)
        change = [1]*n
        ___ i __ r..(n):
            change[(i-arr[i]+1)%n] -= 1
        ___ i __ r..(1, n):
            change[i] += change[i-1]
        r.. change.index(max(change))
    
    # This EASY solution is TLE    
    ___ bestRotation_slow(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        arr = A
        idx, maxVal = 0, float('-inf')
        ___ i __ r..(l..(arr)):
            val = self.getScore(arr, i)
            __ val > maxVal:
                maxVal = val
                idx = i
        r.. idx
    
    ___ getScore(self, arr, k):
        res = 0
        arr0 = arr[k:]+arr[:k]
        ___ i, num __ enumerate(arr0):
            __ num <= i: res += 1
        r.. res
    
    ___ test(self):
        testCases = [
            [2, 3, 1, 4, 0],
            [1, 3, 0, 2, 4],
        ]
        ___ arr __ testCases:
            print('arr: %s' % arr)
            result = self.bestRotation(arr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
