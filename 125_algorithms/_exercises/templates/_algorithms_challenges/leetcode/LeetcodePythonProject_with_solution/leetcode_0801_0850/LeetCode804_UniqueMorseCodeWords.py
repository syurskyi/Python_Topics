'''
Created on Apr 23, 2018

@author: tongq
'''
class Solution(object):
    ___ uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hashset = set()
        for word in words:
            tmp = ''
            for c in word:
                tmp += code[ord(c)-ord('a')]
            hashset.add(tmp)
        return len(hashset)
    
    ___ test(self):
        testCases = [
            ["gin", "zen", "gig", "msg"],
        ]
        for words in testCases:
            print('words: %s' % words)
            result = self.uniqueMorseRepresentations(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
