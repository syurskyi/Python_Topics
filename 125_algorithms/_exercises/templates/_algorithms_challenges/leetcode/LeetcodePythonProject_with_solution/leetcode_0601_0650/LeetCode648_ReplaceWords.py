'''
Created on Oct 2, 2017

@author: MT
'''
c_ Solution(o..
    ___ replaceWords  d.., sentence
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        d...s..(key=l.... x: l..(x
        resArr    # list
        words sentence.s..(' ')
        ___ i, word __ e..(words
            ___ s __ d..:
                __ word[:l..(s)] __ s:
                    resArr.a..(s)
                    _____
            __ i+1 > l..(resArr
                resArr.a..(word)
        r.. ' '.j..(resArr)
    
    ___ test
        testCases [
            [
                ["cat", "bat", "rat"],
                "the cattle was rattled by the battery",
            ],
        ]
        ___ d.., sentence __ testCases:
            print('dict: %s' % d..)
            print('sentence: %s' % sentence)
            result replaceWords(d.., sentence)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
