'''
Created on May 24, 2018

@author: tongq
'''
class Solution(object
    ___ findLadders(self, beginWord, endWord, wordList
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordSet = set(wordList)
        wordSet.add(beginWord)
        distance = {}
        self.bfs(beginWord, endWord, distance, wordSet)
        res = []
        self.dfs(beginWord, endWord, distance, wordSet, res, [])
        r_ res
    
    ___ bfs(self, beginWord, endWord, distance, wordSet
        queue = [beginWord]
        distance[beginWord] = 0
        w___ queue:
            word = queue.pop(0)
            nextWords = self.getNextWords(word, wordSet)
            for nextWord in nextWords:
                __ nextWord not in distance:
                    distance[nextWord] = distance[word]+1
                    queue.append(nextWord)
    
    ___ dfs(self, beginWord, word, distance, wordSet, res, curr
        curr.insert(0, word)
        __ word __ beginWord:
            res.append(list(curr))
        ____
            for nextWord in self.getNextWords(word, wordSet
                __ nextWord in distance and distance[nextWord]+1 __ distance.get(word, 0
                    self.dfs(beginWord, nextWord, distance, wordSet, res, curr)
        curr.pop(0)
    
    ___ getNextWords(self, word, wordSet
        res = []
        for i, c in enumerate(word
            for c0 in 'abcdefghijklmnopqrstuvwxyz':
                __ c0 != c:
                    word0 = word[:i] + c0 + word[i+1:]
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
        ]
        for beginWord, endWord, wordList in testCases:
            result = self.findLadders(beginWord, endWord, wordList)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
