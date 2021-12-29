'''
Created on May 21, 2018

@author: tongq
'''
class Solution(object):
    ___ compareVersion(self, version1, version2):
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
            __ int(arr1[i]) > int(arr2[j]):
                r.. 1
            ____ int(arr1[i]) < int(arr2[j]):
                r.. -1
            ____:
                i += 1
                j += 1
        w.... i < m a.. int(arr1[i]) __ 0:
            i += 1
        w.... j < n a.. int(arr2[j]) __ 0:
            j += 1
        __ i __ m a.. j __ n:
            r.. 0
        ____ i __ m:
            r.. -1
        ____:
            r.. 1
