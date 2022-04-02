'''
Created on Apr 16, 2018

@author: tongq
'''
c_ Solution(o..
    ___ numMatchingSubseq  S, words
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        hashmap    # dict
        ___ i __ r..(26
            c = chr(o..('a')+i)
            hashmap[c]    # list
        ___ word __ words:
            hashmap[word[0]].a..(word)
        count = 0
        ___ c __ S:
            d.. = hashmap[c]
            size = l..(d..)
            ___ i __ r..(size
                word = d...pop(0)
                __ l..(word) __ 1:
                    count += 1
                ____:
                    hashmap[word[1]].a..(word[1:])
        r.. count
    
    ___ test
        testCases = [
            [
                'abcde',
                ["a", "bb", "acd", "ace"],
            ],
        ]
        ___ s, words __ testCases:
            result = numMatchingSubseq(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
