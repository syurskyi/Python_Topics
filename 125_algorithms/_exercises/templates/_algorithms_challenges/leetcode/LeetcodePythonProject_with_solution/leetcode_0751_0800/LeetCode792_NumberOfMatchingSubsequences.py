'''
Created on Apr 16, 2018

@author: tongq
'''
class Solution(object):
    ___ numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        hashmap = {}
        for i in range(26):
            c = chr(ord('a')+i)
            hashmap[c] = []
        for word in words:
            hashmap[word[0]].append(word)
        count = 0
        for c in S:
            deque = hashmap[c]
            size = len(deque)
            for i in range(size):
                word = deque.pop(0)
                __ len(word) == 1:
                    count += 1
                else:
                    hashmap[word[1]].append(word[1:])
        return count
    
    ___ test(self):
        testCases = [
            [
                'abcde',
                ["a", "bb", "acd", "ace"],
            ],
        ]
        for s, words in testCases:
            result = self.numMatchingSubseq(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
