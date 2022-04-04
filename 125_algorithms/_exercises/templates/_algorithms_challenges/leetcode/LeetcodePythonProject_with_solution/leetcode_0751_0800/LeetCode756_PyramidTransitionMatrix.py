'''
Created on Mar 30, 2018

@author: tongq
'''
c_ Solution(o..
    ___ pyramidTransition  bottom, allowed
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        __ n.. bottom:
            r.. F..
        hashmap    # dict
        ___ s __ allowed:
            __ s[:2] __ hashmap:
                hashmap[s[:2]].add(s[-1])
            ____
                hashmap[s[:2]] = s..([s[-1]])
        level = l..(bottom)
        queue = l..(bottom)
        w.... queue:
            __ level __ 1:
                __ queue a.. queue[0]:
                    r.. T..
                ____
                    r.. F..
            nextQueue = [s..() ___ _ __ r..(level-1)]
            ___ i __ r..(level-1
                arr1 = queue[i]
                arr2 = queue[i+1]
                ___ c1 __ arr1:
                    ___ c2 __ arr2:
                        __ c1+c2 __ hashmap:
                            nextQueue[i] = nextQueue[i].union(hashmap[c1+c2])
                __ n.. nextQueue[i]:
                    r.. F..
            queue = nextQueue
            level -= 1
        r.. T..
    
    ___ test
        testCases = [
            [ "XYZ", ["XYD", "YZE", "DEA", "FFF"], ],
            [ 'XXYX', ["XXX", "XXY", "XYX", "XYY", "YXZ"], ],
            [
                "CCC",
                ["CBB","ACB","ABD","CDB","BDC","CBC","DBA","DBB","CAB","BCB","BCC","BAA","CCD","BDD","DDD","CCA","CAA","CCC","CCB"]
            ],
        ]
        ___ bottom, allowed __ testCases:
            print('bottom: %s' % bottom)
            print('allowed: %s' % allowed)
            result = pyramidTransition(bottom, allowed)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
