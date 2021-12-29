'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object):
    ___ pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        __ n.. bottom:
            r.. False
        hashmap = {}
        ___ s __ allowed:
            __ s[:2] __ hashmap:
                hashmap[s[:2]].add(s[-1])
            ____:
                hashmap[s[:2]] = set([s[-1]])
        level = l..(bottom)
        queue = l..(bottom)
        while queue:
            __ level __ 1:
                __ queue and queue[0]:
                    r.. True
                ____:
                    r.. False
            nextQueue = [set() ___ _ __ r..(level-1)]
            ___ i __ r..(level-1):
                arr1 = queue[i]
                arr2 = queue[i+1]
                ___ c1 __ arr1:
                    ___ c2 __ arr2:
                        __ c1+c2 __ hashmap:
                            nextQueue[i] = nextQueue[i].union(hashmap[c1+c2])
                __ n.. nextQueue[i]:
                    r.. False
            queue = nextQueue
            level -= 1
        r.. True
    
    ___ test(self):
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
            result = self.pyramidTransition(bottom, allowed)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
