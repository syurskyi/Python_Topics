'''
Created on Mar 21, 2017

@author: MT
'''

c_ Solution(o..
    ___ reverseVowels  s
        vowels = s..( 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U' )
        __ n.. s: r.. s
        s = l..(s)
        left, right = 0, l..(s)-1
        w.... left < right:
            w.... left < l..(s) a.. s[left] n.. __ vowels:
                left += 1
            w.... right >= 0 a.. s[right] n.. __ vowels:
                right -= 1
            __ left < right:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        r.. ''.j..(s)