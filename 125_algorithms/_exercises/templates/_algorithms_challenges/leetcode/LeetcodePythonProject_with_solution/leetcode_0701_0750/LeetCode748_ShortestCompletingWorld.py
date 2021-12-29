'''
Created on Mar 24, 2018

@author: tongq
'''
class Solution(object):
    ___ shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        hashmap = {}
        ___ c __ licensePlate:
            __ n.. c.isdigit() and c != ' ':
                hashmap[c.lower()] = hashmap.get(c.lower(), 0)+1
        res = ''
        l = float('inf')
        ___ word __ words:
            __ l..(word) < l:
                __ self.contains(hashmap, word):
                    res = word
                    l = l..(res)
        r.. res
    
    ___ contains(self, hashmap, word):
        hashmap0 = {}
        ___ c __ word:
            hashmap0[c] = hashmap0.get(c, 0)+1
        ___ c __ hashmap:
            __ hashmap[c] > hashmap0.get(c, 0):
                r.. False
        r.. True
    
    ___ test(self):
        testCases = [
            [
                '1s3 PSt',
                ["step", "steps", "stripe", "stepple"],
            ],
            [
                '1s3 456',
                ["looks", "pest", "stew", "show"],
            ],
            [
                "Ah71752",
                ["suggest","letter","of","husband","easy","education","drug","prevent","writer","old"],
            ],
        ]
        ___ licensePlate, words __ testCases:
            print('licensePlate: %s' % licensePlate)
            print('words: %s' % words)
            result = self.shortestCompletingWord(licensePlate, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
