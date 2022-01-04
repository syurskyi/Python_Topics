'''
Created on Mar 13, 2018

@author: tongq
'''
c_ Solution(object):
    ___ areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ l..(words1) != l..(words2):
            r.. F..
        pairInfo    # dict
        ___ p __ pairs:
            __ p[0] n.. __ pairInfo:
                pairInfo[p[0]] = set()
            __ p[1] n.. __ pairInfo:
                pairInfo[p[1]] = set()
            pairInfo[p[0]].add(p[1])
            pairInfo[p[1]].add(p[0])
        ___ w1, w2 __ z..(words1, words2):
            __ w1 __ w2:
                _____
            __ w1 n.. __ pairInfo:
                r.. F..
            __ n.. dfs(w1, w2, pairInfo, set()):
                r.. F..
        r.. T..
    
    ___ dfs(self, source, target, pairInfo, visited):
        __ target __ pairInfo.get(source, set()):
            r.. T..
        visited.add(source)
        ___ nextWord __ pairInfo.get(source, set()):
            __ nextWord n.. __ visited a.. dfs(nextWord, target, pairInfo, visited):
                r.. T..
        r.. F..
    
    # This is Exceeding Time Limit
    ___ areSentencesSimilarTwo_own(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ l..(words1) != l..(words2):
            r.. F..
        hashmap    # dict
        n = 0
        l    # list
        ___ p __ pairs:
            __ p[0] n.. __ hashmap:
                l.a..(p[0])
                hashmap[p[0]] = n
                n += 1
            __ p[1] n.. __ hashmap:
                l.a..(p[1])
                hashmap[p[1]] = n
                n += 1
        roots = [-1]*n
        ___ p __ pairs:
            root0 = getRoot(roots, hashmap[p[0]])
            root1 = getRoot(roots, hashmap[p[1]])
            roots[root0] = root1
        ___ w1, w2 __ z..(words1, words2):
            __ w1 __ w2:
                _____
            ____ w1 n.. __ hashmap o. w2 n.. __ hashmap:
                r.. F..
            ____:
                r1 = getRoot(roots, hashmap[w1])
                r2 = getRoot(roots, hashmap[w2])
                __ r1 != r2:
                    r.. F..
        r.. T..
    
    ___ getRoot(self, roots, ind):
        w.... roots[ind] != -1:
            ind = roots[ind]
        r.. ind
    
    ___ test
        testCases = [
            [
                ["great", "acting", "skills"],
                ["fine", "drama", "talent"],
                [
                    ["great",   "good"],
                    ["fine",    "good"],
                    ["acting",  "drama"],
                    ["skills",  "talent"],
                ],
            ],
            [
                ["an","extraordinary","meal","meal"],
                ["one","good","dinner"],
                [
                    ["great","good"],
                    ["extraordinary","good"],
                    ["well","good"],
                    ["wonderful","good"],
                    ["excellent","good"],
                    ["fine","good"],
                    ["nice","good"],
                    ["any","one"],
                    ["some","one"],
                    ["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],["extremely","very"],["actually","very"],["really","very"],["super","very"]],
            ],
        ]
        ___ words1, words2, pairs __ testCases:
            result = areSentencesSimilarTwo(words1, words2, pairs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
