'''
Created on May 17, 2018

@author: tongq
'''
c_ Solution(o..
    ___ reverseWords  s
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        left 0
        i 0
        w.... i < l..(s
            __ s[i] __ ' ':
                reverse(s, left, i-1)
                left i+1
            i += 1
        reverse(s, left, l..(s)-1)
        reverse(s, 0, l..(s)-1)
    
    ___ reverse  s, i, j
        w.... i < j:
            s[i], s[j] s[j], s[i]
            i += 1
            j -_ 1
