'''
Created on Sep 4, 2017

@author: MT
'''
c_ Solution(o..):
    ___ killProcess  pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        hashmap    # dict
        ___ p, pp __ z..(pid, ppid):
            hashset = hashmap.get(pp, s..())
            hashset.add(p)
            hashmap[pp] = hashset
        __ kill n.. __ hashmap:
            r.. [kill]
        queue = l..(hashmap[kill])
        result = s..([kill])
        w.... queue:
            node = queue.pop(0)
            result.add(node)
            ___ node0 __ hashmap.get(node, []):
                __ node0 n.. __ result:
                    queue.a..(node0)
        r.. l..(result)
    
    ___ test
        testCases = [
            [
                [1, 3, 10, 5],
                [3, 0, 5,  3],
                5,
            ],
        ]
        ___ pid, ppid, kill __ testCases:
            print('pid: %s' % pid)
            print('ppid: %s' % ppid)
            print('kill: %s' % kill)
            result = killProcess(pid, ppid, kill)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
