'''
Created on Apr 23, 2018

@author: tongq
'''
c_ Solution(o..
    ___ uniqueMorseRepresentations  words
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hashset = s..()
        ___ word __ words:
            tmp  ''
            ___ c __ word:
                tmp += code[o..(c)-o..('a')]
            hashset.add(tmp)
        r.. l..(hashset)
    
    ___ test
        testCases = [
            ["gin", "zen", "gig", "msg"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = uniqueMorseRepresentations(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
