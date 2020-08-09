'''
Created on May 1, 2018

@author: tongq
'''
class Solution(object
    ___ mostCommonWord(self, paragraph, banned
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
        ___ j in range(le.(paragraph)):
            c = paragraph[j]
            __ not (ord('a') <= ord(c) <= ord('z') or\
                ord('A') <= ord(c) <= ord('Z')):
                word = paragraph[i:j].lower()
                __ word and word not in banned:
                    hashmap[word] = hashmap.get(word, 0)+1
                    __ hashmap[word] > freq:
                        res = word
                        freq = hashmap[word]
                i = j+1
        word = paragraph[i:].lower()
        __ word and word not in banned:
            hashmap[word] = hashmap.get(word, 0)+1
            __ hashmap[word] > freq:
                res = word
                freq = hashmap[word]
        r_ res
