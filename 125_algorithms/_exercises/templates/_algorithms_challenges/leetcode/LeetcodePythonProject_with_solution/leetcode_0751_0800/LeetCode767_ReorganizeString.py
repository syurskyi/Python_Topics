'''
Created on Apr 3, 2018

@author: tongq
'''
c_ Solution(object):
    ___ reorganizeString  S):
        """
        :type S: str
        :rtype: str
        """
        _______ heapq
        s = S
        hashmap    # dict
        ___ c __ s:
            hashmap[c] = hashmap.get(c, 0)+1
        heap    # list
        ___ c, freq __ hashmap.i..:
            heapq.heappush(heap, [-freq, c])
        res = ''
        w.... heap:
            freq1, c1 = heapq.heappop(heap)
            __ res a.. res[-1] __ c1:
                r.. ''
            res += c1
            __ heap:
                freq2, c2 = heapq.heappop(heap)
                res += c2
                __ freq2+1 < 0:
                    heapq.heappush(heap, [freq2+1, c2])
            __ freq1+1 < 0:
                heapq.heappush(heap, [freq1+1, c1])
        r.. ''.j..(res)
    
    ___ test
        testCases = [
            "vvvlo",
            "aab",
            'aaab',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = reorganizeString(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
