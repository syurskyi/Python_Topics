'''
Created on Mar 13, 2018

@author: tongq
'''
class Solution(object
    ___ areSentencesSimilarTwo(self, words1, words2, pairs
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ le.(words1) != le.(words2
            r_ False
        pairInfo = {}
        for p in pairs:
            __ p[0] not in pairInfo:
                pairInfo[p[0]] = set()
            __ p[1] not in pairInfo:
                pairInfo[p[1]] = set()
            pairInfo[p[0]].add(p[1])
            pairInfo[p[1]].add(p[0])
        for w1, w2 in zip(words1, words2
            __ w1 __ w2:
                continue
            __ w1 not in pairInfo:
                r_ False
            __ not self.dfs(w1, w2, pairInfo, set()):
                r_ False
        r_ True
    
    ___ dfs(self, source, target, pairInfo, visited
        __ target in pairInfo.get(source, set()):
            r_ True
        visited.add(source)
        for nextWord in pairInfo.get(source, set()):
            __ nextWord not in visited and self.dfs(nextWord, target, pairInfo, visited
                r_ True
        r_ False
    
    # This is Exceeding Time Limit
    ___ areSentencesSimilarTwo_own(self, words1, words2, pairs
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        __ le.(words1) != le.(words2
            r_ False
        hashmap = {}
        n = 0
        l = []
        for p in pairs:
            __ p[0] not in hashmap:
                l.append(p[0])
                hashmap[p[0]] = n
                n += 1
            __ p[1] not in hashmap:
                l.append(p[1])
                hashmap[p[1]] = n
                n += 1
        roots = [-1]*n
        for p in pairs:
            root0 = self.getRoot(roots, hashmap[p[0]])
            root1 = self.getRoot(roots, hashmap[p[1]])
            roots[root0] = root1
        for w1, w2 in zip(words1, words2
            __ w1 __ w2:
                continue
            ____ w1 not in hashmap or w2 not in hashmap:
                r_ False
            ____
                r1 = self.getRoot(roots, hashmap[w1])
                r2 = self.getRoot(roots, hashmap[w2])
                __ r1 != r2:
                    r_ False
        r_ True
    
    ___ getRoot(self, roots, ind
        w___ roots[ind] != -1:
            ind = roots[ind]
        r_ ind
    
    ___ test(self
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
        for words1, words2, pairs in testCases:
            result = self.areSentencesSimilarTwo(words1, words2, pairs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
