'''
Created on Oct 10, 2018

@author: tongq
'''
______ itertools

class Solution(object
    ___ numSimilarGroups(self, A
        """
        :type A: List[str]
        :rtype: int
        """
        arr = list(set(A))
        parents = {x: x ___ x in arr}
        n, m = le.(arr), le.(arr[0])
        self.count = n
        
        ___ find(x
            __ x != parents[x]:
                parents[x] = find(parents[x])
            r_ parents[x]
        
        ___ union(x, y
            x, y = find(x), find(y)
            __ x != y:
                parents[x] = y
                self.count -= 1
                r_ True
            r_ False
        
        ___ similar(x, y
            r_ su.(i != j ___ i, j in zip(x, y)) __ 2
        
        ## Solution part ##
        __ n < m:
            ___ x, y in itertools.combinations(arr, 2
                __ similar(x, y
                    union(x, y)
        ____
            ___ x in arr:
                ___ i, j in itertools.combinations(range(m), 2
                    y = x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    __ y in parents:
                        union(x, y)
        
        r_ self.count
    
    ___ test(self
        testCases = [
            ["aaa", "aaa", "aaa"],
            ["tars","rats","arts","star"],
            ["blw","bwl","wlb"],
            ["nmiwx","mniwx","wminx","mnixw","xnmwi"],
        ]
        ___ strs in testCases:
            print('strs: %s' % strs)
            result = self.numSimilarGroups(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
