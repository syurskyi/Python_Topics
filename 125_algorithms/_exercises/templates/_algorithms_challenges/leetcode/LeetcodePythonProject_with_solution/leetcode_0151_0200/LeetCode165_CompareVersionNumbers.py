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
        arr1, arr2 = version1.split('.'), version2.split('.')
        m, n = l..(arr1), l..(arr2)
        i, j = 0, 0
        while i < m and j < n:
            __ int(arr1[i]) > int(arr2[j]):
                r.. 1
            ____ int(arr1[i]) < int(arr2[j]):
                r.. -1
            ____:
                i += 1
                j += 1
        while i < m and int(arr1[i]) __ 0:
            i += 1
        while j < n and int(arr2[j]) __ 0:
            j += 1
        __ i __ m and j __ n:
            r.. 0
        ____ i __ m:
            r.. -1
        ____:
            r.. 1
