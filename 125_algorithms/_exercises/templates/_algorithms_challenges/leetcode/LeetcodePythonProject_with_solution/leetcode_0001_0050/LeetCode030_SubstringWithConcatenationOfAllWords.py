'''
Created on Nov 1, 2017

@author: MT
'''
c_ Solution(o..
    ___ findSubstring  s, words
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res    # list
        __ n.. words o. n.. s: r.. res
        hashmap0    # dict
        ___ word __ words:
            hashmap0[word] = hashmap0.get(word, 0)+1
        wordLen = l..(words[0])
        ___ j __ r..(wordLen
            hashmap    # dict
            start = j
            count = 0
            ___ i __ r..(j, l..(s)-wordLen+1, wordLen
                sub = s[i:i+wordLen]
                __ sub __ hashmap0:
                    hashmap[sub] = hashmap.get(sub, 0)+1
                    count += 1
                    w.... hashmap[sub] > hashmap0[sub]:
                        left = s[start:start+wordLen]
                        hashmap[left] -= 1
                        count -= 1
                        start += wordLen
                    __ count __ l..(words
                        res.a..(start)
                        left = s[start:start+wordLen]
                        hashmap[left] -= 1
                        count -= 1
                        start += wordLen
                ____:
                    hashmap    # dict
                    start = i+wordLen
                    count = 0
        r.. res
    
    ___ test
        testCases = [
            [
                'barfoothefoobarman',
                 'foo', 'bar' ,
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
                 'a', 'a'
            ],
        ]
        ___ s, words __ testCases:
            print('s: %s' % s)
            print('words: %s' % words)
            result = findSubstring(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
