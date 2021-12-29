'''
Created on Nov 2, 2017

@author: MT
'''
class Solution(object):
    ___ strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        __ haystack == needle or not needle: return 0
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                __ haystack[i+j] == needle[j]:
                    __ j == len(needle)-1:
                        return i
                else:
                    break
        return -1
