'''
Created on Mar 27, 2018

@author: tongq
'''
c_ Solution(object):
    ___ openLock  deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        queue = ['0000']
        level = 0
        visited = set(['0000'])
        deadends = set(deadends)
        __ '0000' __ deadends:
            r.. -1
        w.... queue:
            n = l..(queue)
            ___ _ __ r..(n):
                s = queue.pop(0)
                __ s __ target:
                    r.. level
                ___ i __ r..(4):
                    s01 = i..(s[i])+1
                    __ s01 >= 10:
                        s01 -= 10
                    s01 = s..(s01)
                    s02 = i..(s[i])-1
                    __ s02 < 0:
                        s02 += 10
                    s02 = s..(s02)
                    s0 = s[:i]+s01+s[i+1:]
                    __ s0 n.. __ visited a.. s0 n.. __ deadends:
                        queue.a..(s0)
                        visited.add(s0)
                    s0 = s[:i]+s02+s[i+1:]
                    __ s0 n.. __ visited a.. s0 n.. __ deadends:
                        queue.a..(s0)
                        visited.add(s0)
            level += 1
        r.. -1
    
    ___ test
        testCases = [
            [
                ["0201","0101","0102","1212","2002"],
                "0202",
            ],
            [
                ["8888"],
                "0009",
            ],
            [
                ["8887","8889","8878","8898","8788","8988","7888","9888"],
                "8888",
            ],
            [
                ["0000"],
                "8888",
            ],
        ]
        ___ deadends, target __ testCases:
            result = openLock(deadends, target)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
