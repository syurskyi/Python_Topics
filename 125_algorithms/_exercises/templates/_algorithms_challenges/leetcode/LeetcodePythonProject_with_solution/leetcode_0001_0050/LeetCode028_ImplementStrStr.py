'''
Created on Nov 2, 2017

@author: MT
'''
c_ Solution(o..
    ___ strStr  haystack, needle
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        __ haystack __ needle o. n.. needle: r.. 0
        ___ i __ r..(l..(haystack)-l..(needle)+1
            ___ j __ r..(l..(needle)):
                __ haystack[i+j] __ needle[j]:
                    __ j __ l..(needle)-1:
                        r.. i
                ____:
                    _____
        r.. -1
