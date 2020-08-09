'''
Created on Oct 24, 2017

@author: MT
'''
class Solution(object
    ___ topKFrequent(self, words, k
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap = {}
        for word in words:
            hashmap[word] = hashmap.get(word, 0)+1
        n = le.(words)
        dp = [[] for _ in range(n+1)]
        for word, freq in hashmap.items(
            dp[freq].append(word)
        res = []
        for i in range(n, -1, -1
            __ dp[i]:
                dp[i].sort()
                res += dp[i]
                __ le.(res) >= k:
                    break
        r_ res[:k]
    
    ___ test(self
        testCases = [
            [
                ["i", "love", "leetcode", "i", "love", "coding"],
                2,
            ],
            [
                ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
                4
            ],
        ]
        for words, k in testCases:
            print('words: %s' % words)
            print('k: %s' % k)
            result = self.topKFrequent(words, k)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
