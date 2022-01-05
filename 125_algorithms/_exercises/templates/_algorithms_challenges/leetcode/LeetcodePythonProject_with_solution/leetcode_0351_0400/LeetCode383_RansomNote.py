'''
Created on Apr 2, 2017

@author: MT
'''

c_ Solution(o..):
    ___ canConstruct  ransomNote, magazine):
        hashmap    # dict
        ___ c __ magazine:
            hashmap[c] = hashmap.get(c, 0)+1
        ___ c __ ransomNote:
            __ c n.. __ hashmap:
                r.. F..
            hashmap[c] -= 1
            __ hashmap[c] __ 0:
                del hashmap[c]
        r.. T..
