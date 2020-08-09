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
        for s in allowed:
            __ s[:2] in hashmap:
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
            nextQueue = [set() for _ in range(level-1)]
            for i in range(level-1
                arr1 = queue[i]
                arr2 = queue[i+1]
                for c1 in arr1:
                    for c2 in arr2:
                        __ c1+c2 in hashmap:
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
        for bottom, allowed in testCases:
            print('bottom: %s' % bottom)
            print('allowed: %s' % allowed)
            result = self.pyramidTransition(bottom, allowed)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
