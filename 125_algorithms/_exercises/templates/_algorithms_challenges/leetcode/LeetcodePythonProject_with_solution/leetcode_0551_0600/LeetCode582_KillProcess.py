'''
Created on Sep 4, 2017

@author: MT
'''
class Solution(object):
    ___ killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        hashmap = {}
        ___ p, pp __ zip(pid, ppid):
            hashset = hashmap.get(pp, set())
            hashset.add(p)
            hashmap[pp] = hashset
        __ kill n.. __ hashmap:
            r.. [kill]
        queue = l..(hashmap[kill])
        result = set([kill])
        while queue:
            node = queue.pop(0)
            result.add(node)
            ___ node0 __ hashmap.get(node, []):
                __ node0 n.. __ result:
                    queue.a..(node0)
        r.. l..(result)
    
    ___ test(self):
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
            result = self.killProcess(pid, ppid, kill)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
