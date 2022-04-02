'''
Created on Apr 20, 2017

@author: MT
'''

c_ Solution(o..
    ___ frequencySort  s
        hashmap    # dict
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        bucket = [[] ___ _ __ r..(l..(s)+1)]
        ___ c, count __ hashmap.i..:
            bucket[count].a..(c)
        result = ''
        ___ i __ r..(l..(bucket)-1, -1, -1
            w.... bucket[i]:
                c = bucket[i].pop()
                result += c*(i)
        r.. result
    
    ___ test
        testCases = [
            'aaaa',
            'tree',
            'cccaaa',
            'Aabb',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = frequencySort(s)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()


