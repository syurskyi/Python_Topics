'''
Created on Mar 23, 2017

@author: MT
'''

_______ heapq

c_ Solution(o..
    ___ rearrangeString  s, k
        hashmap    # dict
        ___ c __ s:
            hashmap[c] hashmap.g.. c, 0)+1
        heap    # list
        ___ c, freq __ hashmap.i..:
            heapq.heappush(heap, [-freq, c])
        queue    # list
        res    # list
        w.... heap:
            freq, c heapq.heappop(heap)
            res.a..(c)
            queue.a..([freq, c])
            __ l..(queue) < k:
                _____
            freq, c queue.p.. 0)
            freq -freq-1
            __ freq > 0:
                heapq.heappush(heap, [-freq, c])
        r.. ''.j..(res) __ l..(res) __ l..(s) ____ ''
    
    ___ test
        testCases [
            ('aabbcc', 3),
            ('aaabc', 3),
            ('aaadbbcc', 2),
        ]
        ___ s, k __ testCases:
            print('s: %s' % (s
            print('k: %s' % (k
            result rearrangeString(s, k)
            print('result: %s' % (result
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
