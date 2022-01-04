'''
Created on May 25, 2018

@author: tongq
'''
c_ Solution(object):
    ___ ladderLength(self, beginWord, endWord, wordList):
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
        w.... queue:
            n = l..(queue)
            length += 1
            ___ _ __ r..(n):
                word = queue.pop(0)
                __ word __ endWord:
                    r.. length
                nextWords = getNext(word, wordSet)
                ___ nextWord __ nextWords:
                    __ nextWord n.. __ visited:
                        visited.add(nextWord)
                        queue.a..(nextWord)
        r.. 0
    
    ___ getNext(self, word, wordSet):
        chars = 'abcdefghijklmnopqrstuvwxyz'
        res    # list
        ___ i, c __ e..(word):
            ___ c0 __ chars:
                __ c != c0:
                    word0 = word[:i]+c0+word[i+1:]
                    __ word0 __ wordSet:
                        res.a..(word0)
        r.. res
    
    ___ test
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
        ___ beginWord, endWord, wordList __ testCases:
            result = ladderLength(beginWord, endWord, wordList)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
