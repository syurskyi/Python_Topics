'''
Created on Mar 30, 2018

@author: tongq
'''
class Solution(object
    ___ pyramidTransition(self, bottom, allowed
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        __ not bottom:
            r_ False
        hashmap = {}
        ___ s __ allowed:
            __ s[:2] __ hashmap:
                hashmap[s[:2]].add(s[-1])
            ____
                hashmap[s[:2]] = set([s[-1]])
        level = le.(bottom)
        queue = list(bottom)
        w___ queue:
            __ level __ 1:
                __ queue and queue[0]:
                    r_ True
                ____
                    r_ False
            nextQueue = [set() ___ _ __ range(level-1)]
            ___ i __ range(level-1
                arr1 = queue[i]
                arr2 = queue[i+1]
                ___ c1 __ arr1:
                    ___ c2 __ arr2:
                        __ c1+c2 __ hashmap:
                            nextQueue[i] = nextQueue[i].union(hashmap[c1+c2])
                __ not nextQueue[i]:
                    r_ False
            queue = nextQueue
            level -= 1
        r_ True
    
    ___ test(self
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

__  -n __ '__main__':
    Solution().test()
