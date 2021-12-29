'''
Created on May 2, 2018

@author: tongq
'''
class Solution(object):
    ___ minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        hashset = set(words)
        for word in words:
            for i in range(1, len(word)):
                hashset.discard(word[i:])
        res = 0
        for word in hashset:
            res += len(word)+1
        return res
    
    ___ test(self):
        testCases = [
            ["time", "me", "bell"],
            ["me", "time"],
        ]
        for words in testCases:
            print('words: %s' % words)
            result = self.minimumLengthEncoding(words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
