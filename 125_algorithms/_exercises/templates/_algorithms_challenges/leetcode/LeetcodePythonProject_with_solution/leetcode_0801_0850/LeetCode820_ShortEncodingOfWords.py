'''
Created on May 2, 2018

@author: tongq
'''
c_ Solution(o..
    ___ minimumLengthEncoding  words
        """
        :type words: List[str]
        :rtype: int
        """
        hashset = s..(words)
        ___ word __ words:
            ___ i __ r..(1, l..(word:
                hashset.discard(word[i:])
        res = 0
        ___ word __ hashset:
            res += l..(word)+1
        r.. res
    
    ___ test
        testCases = [
            ["time", "me", "bell"],
            ["me", "time"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = minimumLengthEncoding(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
