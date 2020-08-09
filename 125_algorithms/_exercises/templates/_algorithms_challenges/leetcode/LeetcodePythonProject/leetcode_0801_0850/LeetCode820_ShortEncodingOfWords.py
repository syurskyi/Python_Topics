'''
Created on May 2, 2018

@author: tongq
'''
class Solution(object
    ___ minimumLengthEncoding(self, words
        """
        :type words: List[str]
        :rtype: int
        """
        hashset = set(words)
        ___ word in words:
            ___ i in range(1, le.(word)):
                hashset.discard(word[i:])
        res = 0
        ___ word in hashset:
            res += le.(word)+1
        r_ res
    
    ___ test(self
        testCases = [
            ["time", "me", "bell"],
            ["me", "time"],
        ]
        ___ words in testCases:
            print('words: %s' % words)
            result = self.minimumLengthEncoding(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
