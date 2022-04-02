'''
Created on May 21, 2018

@author: tongq
'''
c_ Solution(o..
    ___ compareVersion  version1, version2
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        __ version1 __ version2: r.. 0
        arr1, arr2 = version1.s..('.'), version2.s..('.')
        m, n = l..(arr1), l..(arr2)
        i, j = 0, 0
        w.... i < m a.. j < n:
            __ i..(arr1[i]) > i..(arr2[j]
                r.. 1
            ____ i..(arr1[i]) < i..(arr2[j]
                r.. -1
            ____:
                i += 1
                j += 1
        w.... i < m a.. i..(arr1[i]) __ 0:
            i += 1
        w.... j < n a.. i..(arr2[j]) __ 0:
            j += 1
        __ i __ m a.. j __ n:
            r.. 0
        ____ i __ m:
            r.. -1
        ____:
            r.. 1
