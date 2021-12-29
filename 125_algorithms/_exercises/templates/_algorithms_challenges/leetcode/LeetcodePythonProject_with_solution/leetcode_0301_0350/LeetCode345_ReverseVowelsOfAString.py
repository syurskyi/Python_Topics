'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object):
    ___ reverseVowels(self, s):
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        __ n.. s: r.. s
        s = l..(s)
        left, right = 0, l..(s)-1
        while left < right:
            while left < l..(s) and s[left] n.. __ vowels:
                left += 1
            while right >= 0 and s[right] n.. __ vowels:
                right -= 1
            __ left < right:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        r.. ''.join(s)