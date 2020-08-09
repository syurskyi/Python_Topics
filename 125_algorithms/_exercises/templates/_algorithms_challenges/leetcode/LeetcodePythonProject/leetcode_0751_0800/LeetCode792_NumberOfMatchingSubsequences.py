'''
Created on Apr 16, 2018

@author: tongq
'''
class Solution(object
    ___ numMatchingSubseq(self, S, words
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        hashmap = {}
        ___ i in range(26
            c = chr(ord('a')+i)
            hashmap[c] = []
        ___ word in words:
            hashmap[word[0]].append(word)
        count = 0
        ___ c in S:
            deque = hashmap[c]
            size = le.(deque)
            ___ i in range(size
                word = deque.pop(0)
                __ le.(word) __ 1:
                    count += 1
                ____
                    hashmap[word[1]].append(word[1:])
        r_ count
    
    ___ test(self
        testCases = [
            [
                'abcde',
                ["a", "bb", "acd", "ace"],
            ],
        ]
        ___ s, words in testCases:
            result = self.numMatchingSubseq(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
