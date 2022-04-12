'''
Created on Oct 10, 2018

@author: tongq
'''
_______ i..

c_ Solution(o..
    ___ numSimilarGroups  A
        """
        :type A: List[str]
        :rtype: int
        """
        arr l..(s..(A
        parents {x: x ___ x __ arr}
        n, m l..(arr), l..(arr 0
        count n
        
        ___ find(x
            __ x !_ parents[x]:
                parents[x] find(parents[x])
            r.. parents[x]
        
        ___ union(x, y
            x, y find(x), find(y)
            __ x !_ y:
                parents[x] y
                count -_ 1
                r.. T..
            r.. F..
        
        ___ similar(x, y
            r.. s..(i !_ j ___ i, j __ z..(x, y __ 2
        
        ## Solution part ##
        __ n < m:
            ___ x, y __ i...c..arr, 2
                __ similar(x, y
                    union(x, y)
        ____
            ___ x __ arr:
                ___ i, j __ i...c..r..(m), 2
                    y x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    __ y __ parents:
                        union(x, y)
        
        r.. count
    
    ___ test
        testCases [
            ["aaa", "aaa", "aaa"],
            ["tars","rats","arts","star"],
            ["blw","bwl","wlb"],
            ["nmiwx","mniwx","wminx","mnixw","xnmwi"],
        ]
        ___ strs __ testCases:
            print('strs: %s' % strs)
            result numSimilarGroups(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
