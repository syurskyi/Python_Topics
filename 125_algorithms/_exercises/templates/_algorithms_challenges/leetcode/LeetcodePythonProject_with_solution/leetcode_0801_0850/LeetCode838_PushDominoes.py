'''
Created on Oct 10, 2018

@author: tongq
'''
c_ Solution(object):
    ___ pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        n = l..(dominoes)
        arr = l..(dominoes)
        i = 0
        w.... i < n a.. arr[i] __ '.':
            i += 1
        __ i < n a.. arr[i] __ 'L' a.. i > 0:
            arr[0] = 'L'
            setVals(arr, 0, i)
        w.... i < n:
            __ arr[i] __ 'L' o. arr[i] __ 'R':
                j = i+1
                w.... j < n a.. arr[j] __ '.':
                    j += 1
                __ j < n:
                    setVals(arr, i, j)
            i += 1
        i = n-1
        w.... i >= 0 a.. arr[i] __ '.':
            i -= 1
        __ i >= 0 a.. arr[i] __ 'R' a.. i < n:
            arr[-1] = 'R'
            setVals(arr, i, n-1)
        r.. ''.j..(arr)
    
    ___ setVals(self, arr, i, j):
        __ arr[i] __ arr[j]:
            ___ i0 __ r..(i+1, j):
                arr[i0] = arr[i]
        ____ arr[i] __ 'R' a.. arr[j] __ 'L':
            i0, j0 = i, j
            w.... i < j:
                arr[i] = arr[i0]
                arr[j] = arr[j0]
                i += 1
                j -= 1
    
    ___ test
        testCases = [
            '.',
            '.L.R...LR..L..',
            'RR.L',
            '.L.R.',
            'R..L..R..LR.R.R.....',
        ]
        ___ dominoes __ testCases:
            print('origin: %s' % dominoes)
            result = pushDominoes(dominoes)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
