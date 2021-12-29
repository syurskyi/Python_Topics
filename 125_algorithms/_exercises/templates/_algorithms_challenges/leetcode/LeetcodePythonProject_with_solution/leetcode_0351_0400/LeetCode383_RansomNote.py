'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    ___ canConstruct(self, ransomNote, magazine):
        hashmap = {}
        ___ c __ magazine:
            hashmap[c] = hashmap.get(c, 0)+1
        ___ c __ ransomNote:
            __ c n.. __ hashmap:
                r.. False
            hashmap[c] -= 1
            __ hashmap[c] __ 0:
                del hashmap[c]
        r.. True
