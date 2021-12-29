'''
Created on Oct 10, 2018

@author: tongq
'''
_______ itertools

class Solution(object):
    ___ numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        arr = l..(set(A))
        parents = {x: x ___ x __ arr}
        n, m = l..(arr), l..(arr[0])
        self.count = n
        
        ___ find(x):
            __ x != parents[x]:
                parents[x] = find(parents[x])
            r.. parents[x]
        
        ___ union(x, y):
            x, y = find(x), find(y)
            __ x != y:
                parents[x] = y
                self.count -= 1
                r.. True
            r.. False
        
        ___ similar(x, y):
            r.. s..(i != j ___ i, j __ zip(x, y)) __ 2
        
        ## Solution part ##
        __ n < m:
            ___ x, y __ itertools.combinations(arr, 2):
                __ similar(x, y):
                    union(x, y)
        ____:
            ___ x __ arr:
                ___ i, j __ itertools.combinations(r..(m), 2):
                    y = x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    __ y __ parents:
                        union(x, y)
        
        r.. self.count
    
    ___ test(self):
        testCases = [
            ["aaa", "aaa", "aaa"],
            ["tars","rats","arts","star"],
            ["blw","bwl","wlb"],
            ["nmiwx","mniwx","wminx","mnixw","xnmwi"],
        ]
        ___ strs __ testCases:
            print('strs: %s' % strs)
            result = self.numSimilarGroups(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
