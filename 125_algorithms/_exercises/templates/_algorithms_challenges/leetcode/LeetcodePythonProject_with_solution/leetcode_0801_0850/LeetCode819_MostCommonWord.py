'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object):
    ___ mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hashmap = {}
        res = ''
        freq = 0
        banned = set(banned)
        i = 0
        ___ j __ r..(l..(paragraph)):
            c = paragraph[j]
            __ n.. (ord('a') <= ord(c) <= ord('z') o.\
                ord('A') <= ord(c) <= ord('Z')):
                word = paragraph[i:j].lower()
                __ word a.. word n.. __ banned:
                    hashmap[word] = hashmap.get(word, 0)+1
                    __ hashmap[word] > freq:
                        res = word
                        freq = hashmap[word]
                i = j+1
        word = paragraph[i:].lower()
        __ word a.. word n.. __ banned:
            hashmap[word] = hashmap.get(word, 0)+1
            __ hashmap[word] > freq:
                res = word
                freq = hashmap[word]
        r.. res
