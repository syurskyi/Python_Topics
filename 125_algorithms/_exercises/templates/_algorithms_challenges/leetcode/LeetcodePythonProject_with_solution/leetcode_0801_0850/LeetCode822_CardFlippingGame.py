'''
Created on May 2, 2018

@author: tongq
'''
c_ Solution(o..
    ___ flipgame  fronts, backs
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        same = s..()
        ___ f, b __ z..(fronts, backs
            __ f __ b: same.add(f)
        res = f__('inf')
        ___ f, b __ z..(fronts, backs
            __ f n.. __ same:
                res = m..(res, f)
            __ b n.. __ same:
                res = m..(res, b)
        r.. res __ res != f__('inf') ____ 0
    
    ___ flipgame_own_TLE  fronts, backs
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        hashmap1    # dict
        hashmap2    # dict
        ___ f, b __ z..(fronts, backs
            hashmap1[f] = hashmap1.g.. f, 0)+1
            hashmap2[b] = hashmap2.g.. b, 0)+1
        res = f__('inf')
        helper(fronts, backs, 0, hashmap1, hashmap2)
        r.. res __ res != f__('inf') ____ 0
        
    ___ helper  fronts, backs, i, hashmap1, hashmap2
        __ i >_ l..(fronts
            r..
        __ backs[i] n.. __ hashmap1:
            res = m..(res, backs[i])
        helper(fronts, backs, i+1, hashmap1, hashmap2)
        flip(fronts, backs, i, hashmap1, hashmap2)
        helper(fronts, backs, i+1, hashmap1, hashmap2)
        flip(fronts, backs, i, hashmap1, hashmap2)
    
    ___ flip  fronts, backs, i, hashmap1, hashmap2
        f, b = fronts[i], backs[i]
        fronts[i], backs[i] = backs[i], fronts[i]
        hashmap1[b] = hashmap1.g.. b, 0)+1
        hashmap2[f] = hashmap2.g.. f, 0)+1
        hashmap1[f] -= 1
        __ hashmap1[f] __ 0:
            del hashmap1[f]
        hashmap2[b] -= 1
        __ hashmap2[b] __ 0:
            del hashmap2[b]
        __ backs[i] n.. __ hashmap1:
            res = m..(res, backs[i])
    
    ___ test
        testCases = [
            [
                [1,2,4,4,7],
                [1,3,4,1,3],
            ],
            [
                [2,4,5,5,5,6,2,2,1,3,1,2,1,2,4,5,1,4,3,3],
                [3,4,5,6,2,6,5,6,2,3,1,2,3,2,4,5,4,3,5,3],
            ],
        ]
        ___ fronts, backs __ testCases:
            print('fronts: %s' % fronts)
            print('backs: %s' % backs)
            result = flipgame(fronts, backs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
