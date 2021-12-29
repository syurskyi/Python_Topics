'''
Created on Oct 10, 2018

@author: tongq
'''
class Solution(object):
    ___ pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = l..(dominoes)
        arr = l..(dominoes)
        i = 0
        while i < n and arr[i] __ '.':
            i += 1
        __ i < n and arr[i] __ 'L' and i > 0:
            arr[0] = 'L'
            self.setVals(arr, 0, i)
        while i < n:
            __ arr[i] __ 'L' o. arr[i] __ 'R':
                j = i+1
                while j < n and arr[j] __ '.':
                    j += 1
                __ j < n:
                    self.setVals(arr, i, j)
            i += 1
        i = n-1
        while i >= 0 and arr[i] __ '.':
            i -= 1
        __ i >= 0 and arr[i] __ 'R' and i < n:
            arr[-1] = 'R'
            self.setVals(arr, i, n-1)
        r.. ''.join(arr)
    
    ___ setVals(self, arr, i, j):
        __ arr[i] __ arr[j]:
            ___ i0 __ r..(i+1, j):
                arr[i0] = arr[i]
        ____ arr[i] __ 'R' and arr[j] __ 'L':
            i0, j0 = i, j
            while i < j:
                arr[i] = arr[i0]
                arr[j] = arr[j0]
                i += 1
                j -= 1
    
    ___ test(self):
        testCases = [
            '.',
            '.L.R...LR..L..',
            'RR.L',
            '.L.R.',
            'R..L..R..LR.R.R.....',
        ]
        ___ dominoes __ testCases:
            print('origin: %s' % dominoes)
            result = self.pushDominoes(dominoes)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
