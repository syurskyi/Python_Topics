'''
Created on Nov 1, 2017

@author: MT
'''
class Solution(object):
    ___ findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        __ not words or not s: return res
        hashmap0 = {}
        for word in words:
            hashmap0[word] = hashmap0.get(word, 0)+1
        wordLen = len(words[0])
        for j in range(wordLen):
            hashmap = {}
            start = j
            count = 0
            for i in range(j, len(s)-wordLen+1, wordLen):
                sub = s[i:i+wordLen]
                __ sub in hashmap0:
                    hashmap[sub] = hashmap.get(sub, 0)+1
                    count += 1
                    while hashmap[sub] > hashmap0[sub]:
                        left = s[start:start+wordLen]
                        hashmap[left] -= 1
                        count -= 1
                        start += wordLen
                    __ count == len(words):
                        res.append(start)
                        left = s[start:start+wordLen]
                        hashmap[left] -= 1
                        count -= 1
                        start += wordLen
                else:
                    hashmap = {}
                    start = i+wordLen
                    count = 0
        return res
    
    ___ test(self):
        testCases = [
            [
                'barfoothefoobarman',
                ['foo', 'bar'],
            ],
            [
                'barfoofoobarthefoobarman',
                ["bar","foo","the"],
            ],
            [
                "wordgoodgoodgoodbestword",
                ["word","good","best","good"],
            ],
            [
                'aaa',
                ['a', 'a']
            ],
        ]
        for s, words in testCases:
            print('s: %s' % s)
            print('words: %s' % words)
            result = self.findSubstring(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
