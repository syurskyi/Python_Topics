'''
Created on Oct 7, 2019

@author: tongq
'''
c_ Solution(o..
    ___ robotSim  commands, obstacles
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dirs [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pos [0, 0]
        res 0
        d 0
        hashset s..()
        ___ ob __ obstacles:
            hashset.add(t..(ob
        ___ c __ commands:
            __ c __ (-1, -2
                d calDirection(d, c)
            ____
                ___ _ __ r..(c
                    __ (pos[0] + dirs[d][0], pos[1] + dirs[d][1]) n.. __ hashset:
                        pos [pos[0] + dirs[d][0], pos[1] + dirs[d][1]]
            res m..(res, pos[0]**2 + pos[1]**2)
        r.. res
    
    ___ calDirection  d, c
        __ c __ -2:
            d -_ 1
        ____ c __ -1:
            d += 1
        d %= 4
        r.. d
    
    ___ test
        testCases [
            [
                [4,-1,3],
                [],
            ],
        ]
        ___ commands, obstacles __ testCases:
            res robotSim(commands, obstacles)
            print('res: %s' % res)

__ _____ __ _____
    Solution().test()
