'''
Created on Oct 10, 2018

@author: tongq
'''
import itertools

class Solution(object):
    ___ numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        arr = list(set(A))
        parents = {x: x for x in arr}
        n, m = len(arr), len(arr[0])
        self.count = n
        
        ___ find(x):
            __ x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        ___ union(x, y):
            x, y = find(x), find(y)
            __ x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False
        
        ___ similar(x, y):
            return sum(i != j for i, j in zip(x, y)) == 2
        
        ## Solution part ##
        __ n < m:
            for x, y in itertools.combinations(arr, 2):
                __ similar(x, y):
                    union(x, y)
        else:
            for x in arr:
                for i, j in itertools.combinations(range(m), 2):
                    y = x[:i] + x[j] + x[i+1:j] + x[i] + x[j+1:]
                    __ y in parents:
                        union(x, y)
        
        return self.count
    
    ___ test(self):
        testCases = [
            ["aaa", "aaa", "aaa"],
            ["tars","rats","arts","star"],
            ["blw","bwl","wlb"],
            ["nmiwx","mniwx","wminx","mnixw","xnmwi"],
        ]
        for strs in testCases:
            print('strs: %s' % strs)
            result = self.numSimilarGroups(strs)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
