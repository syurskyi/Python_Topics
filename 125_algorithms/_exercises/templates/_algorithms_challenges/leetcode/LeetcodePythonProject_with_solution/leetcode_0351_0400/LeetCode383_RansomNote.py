'''
Created on Apr 2, 2017

@author: MT
'''

class Solution(object):
    ___ canConstruct(self, ransomNote, magazine):
        hashmap = {}
        for c in magazine:
            hashmap[c] = hashmap.get(c, 0)+1
        for c in ransomNote:
            __ c not in hashmap:
                return False
            hashmap[c] -= 1
            __ hashmap[c] == 0:
                del hashmap[c]
        return True
