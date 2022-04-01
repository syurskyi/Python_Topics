'''
Created on Mar 24, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ shortestCompletingWord  licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        hashmap    # dict
        ___ c __ licensePlate:
            __ n.. c.i.. a.. c != ' ':
                hashmap[c.l..] = hashmap.get(c.l.., 0)+1
        res = ''
        l = f__('inf')
        ___ word __ words:
            __ l..(word) < l:
                __ contains(hashmap, word):
                    res = word
                    l = l..(res)
        r.. res
    
    ___ contains  hashmap, word):
        hashmap0    # dict
        ___ c __ word:
            hashmap0[c] = hashmap0.get(c, 0)+1
        ___ c __ hashmap:
            __ hashmap[c] > hashmap0.get(c, 0):
                r.. F..
        r.. T..
    
    ___ test
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
            result = shortestCompletingWord(licensePlate, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
