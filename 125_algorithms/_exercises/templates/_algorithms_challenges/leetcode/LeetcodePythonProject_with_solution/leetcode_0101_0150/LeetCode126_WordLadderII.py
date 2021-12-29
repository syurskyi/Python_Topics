'''
Created on May 24, 2018

@author: tongq
'''
class Solution(object):
    ___ findLadders(self, beginWord, endWord, wordList):
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
        res    # list
        self.dfs(beginWord, endWord, distance, wordSet, res, [])
        r.. res
    
    ___ bfs(self, beginWord, endWord, distance, wordSet):
        queue = [beginWord]
        distance[beginWord] = 0
        while queue:
            word = queue.pop(0)
            nextWords = self.getNextWords(word, wordSet)
            ___ nextWord __ nextWords:
                __ nextWord n.. __ distance:
                    distance[nextWord] = distance[word]+1
                    queue.a..(nextWord)
    
    ___ dfs(self, beginWord, word, distance, wordSet, res, curr):
        curr.insert(0, word)
        __ word __ beginWord:
            res.a..(l..(curr))
        ____:
            ___ nextWord __ self.getNextWords(word, wordSet):
                __ nextWord __ distance and distance[nextWord]+1 __ distance.get(word, 0):
                    self.dfs(beginWord, nextWord, distance, wordSet, res, curr)
        curr.pop(0)
    
    ___ getNextWords(self, word, wordSet):
        res    # list
        ___ i, c __ enumerate(word):
            ___ c0 __ 'abcdefghijklmnopqrstuvwxyz':
                __ c0 != c:
                    word0 = word[:i] + c0 + word[i+1:]
                    __ word0 __ wordSet:
                        res.a..(word0)
        r.. res
    
    ___ test(self):
        testCases = [
            [
                "hit",
                "cog",
                ["hot","dot","dog","lot","log","cog"],
            ],
        ]
        ___ beginWord, endWord, wordList __ testCases:
            result = self.findLadders(beginWord, endWord, wordList)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
