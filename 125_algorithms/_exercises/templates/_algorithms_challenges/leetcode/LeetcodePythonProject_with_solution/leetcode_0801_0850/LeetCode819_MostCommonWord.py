'''
Created on May 1, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ mostCommonWord  paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        hashmap    # dict
        res = ''
        freq = 0
        banned = set(banned)
        i = 0
        ___ j __ r..(l..(paragraph)):
            c = paragraph[j]
            __ n.. (o..('a') <= o..(c) <= o..('z') o.\
                o..('A') <= o..(c) <= o..('Z')):
                word = paragraph[i:j].l..
                __ word a.. word n.. __ banned:
                    hashmap[word] = hashmap.get(word, 0)+1
                    __ hashmap[word] > freq:
                        res = word
                        freq = hashmap[word]
                i = j+1
        word = paragraph[i:].l..
        __ word a.. word n.. __ banned:
            hashmap[word] = hashmap.get(word, 0)+1
            __ hashmap[word] > freq:
                res = word
                freq = hashmap[word]
        r.. res
