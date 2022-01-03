'''
Created on Apr 23, 2018

@author: tongq
'''
c_ Solution(object):
    ___ uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hashset = set()
        ___ word __ words:
            tmp = ''
            ___ c __ word:
                tmp += code[ord(c)-ord('a')]
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

__ __name__ __ '__main__':
    Solution().test()
