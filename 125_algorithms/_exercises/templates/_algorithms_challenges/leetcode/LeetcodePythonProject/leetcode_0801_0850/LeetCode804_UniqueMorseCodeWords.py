'''
Created on Apr 23, 2018

@author: tongq
'''
class Solution(object
    ___ uniqueMorseRepresentations(self, words
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
        r_ le.(hashset)
    
    ___ test(self
        testCases = [
            ["gin", "zen", "gig", "msg"],
        ]
        ___ words __ testCases:
            print('words: %s' % words)
            result = self.uniqueMorseRepresentations(words)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
