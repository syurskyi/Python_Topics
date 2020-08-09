'''
Created on May 31, 2018

@author: tongq
'''
class Solution(object
    ___ isScramble(self, s1, s2
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        __ le.(s1) != le.(s2
            r_ False
        __ le.(s1) __ 0 or s1 __ s2:
            r_ True
        l1 = list(s1)
        l2 = list(s2)
        l1.sort()
        l2.sort()
        __ l1 != l2:
            r_ False
        for i in range(1, le.(s1)):
            s11 = s1[0:i]
            s12 = s1[i:le.(s1)]
            s21 = s2[0:i]
            s22 = s2[i:le.(s2)]
            s23 = s2[0:le.(s2)-i]
            s24 = s2[le.(s2)-i:le.(s2)]
            __ self.isScramble(s11, s21) and self.isScramble(s12, s22
                r_ True
            __ self.isScramble(s11, s24) and self.isScramble(s12, s23
                r_ True
        r_ False
