'''
Created on May 25, 2018

@author: tongq
'''
class Solution(object
    ___ ladderLength(self, beginWord, endWord, wordList
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordSet = set(wordList)
        wordSet.add(beginWord)
        # DON'T ADD endWord
        visited = set([beginWord])
        queue = [beginWord]
        length = 0
        w___ queue:
            n = le.(queue)
            length += 1
            for _ in range(n
                word = queue.pop(0)
                __ word __ endWord:
                    r_ length
                nextWords = self.getNext(word, wordSet)
                for nextWord in nextWords:
                    __ nextWord not in visited:
                        visited.add(nextWord)
                        queue.append(nextWord)
        r_ 0
    
    ___ getNext(self, word, wordSet
        chars = 'abcdefghijklmnopqrstuvwxyz'
        res = []
        for i, c in enumerate(word
            for c0 in chars:
                __ c != c0:
                    word0 = word[:i]+c0+word[i+1:]
                    __ word0 in wordSet:
                        res.append(word0)
        r_ res
    
    ___ test(self
        testCases = [
            [
                "hit",
                "cog",
                ["hot","dot","dog","lot","log","cog"],
            ],
            [
                "hit",
                "cog",
                ["hot","dot","dog","lot","log"],
            ],
        ]
        for beginWord, endWord, wordList in testCases:
            result = self.ladderLength(beginWord, endWord, wordList)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
