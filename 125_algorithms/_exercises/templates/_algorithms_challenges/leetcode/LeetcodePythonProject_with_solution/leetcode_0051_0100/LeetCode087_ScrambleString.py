'''
Created on May 31, 2018

@author: tongq
'''
c_ Solution(object):
    ___ isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        __ l..(s1) != l..(s2):
            r.. F..
        __ l..(s1) __ 0 o. s1 __ s2:
            r.. T..
        l1 = l..(s1)
        l2 = l..(s2)
        l1.s..()
        l2.s..()
        __ l1 != l2:
            r.. F..
        ___ i __ r..(1, l..(s1)):
            s11 = s1[0:i]
            s12 = s1[i:l..(s1)]
            s21 = s2[0:i]
            s22 = s2[i:l..(s2)]
            s23 = s2[0:l..(s2)-i]
            s24 = s2[l..(s2)-i:l..(s2)]
            __ isScramble(s11, s21) a.. isScramble(s12, s22):
                r.. T..
            __ isScramble(s11, s24) a.. isScramble(s12, s23):
                r.. T..
        r.. F..
