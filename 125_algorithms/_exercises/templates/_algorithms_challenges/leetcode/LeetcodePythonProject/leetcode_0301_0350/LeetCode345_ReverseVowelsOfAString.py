'''
Created on Mar 21, 2017

@author: MT
'''

class Solution(object
    ___ reverseVowels(self, s
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        __ not s: r_ s
        s = list(s)
        left, right = 0, le.(s)-1
        w___ left < right:
            w___ left < le.(s) and s[left] not in vowels:
                left += 1
            w___ right >= 0 and s[right] not in vowels:
                right -= 1
            __ left < right:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        r_ ''.join(s)