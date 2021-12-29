'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    ___ minTransfers(self, transactions):
        bal = {}
        ___ tran __ transactions:
            bal[tran[0]] = bal.get(tran[0], 0)+tran[2]
            bal[tran[1]] = bal.get(tran[1], 0)-tran[2]
        self.debt    # list
        ___ count __ bal.values():
            self.debt.a..(count)
        r.. self.dfs(0, 0)
        
    ___ dfs(self, s, cnt):
        while s < l..(self.debt) and self.debt[s] __ 0:
            s += 1
        res = float('inf')
        prev = 0
        ___ i __ r..(s+1, l..(self.debt)):
            __ self.debt[i] != prev and self.debt[i]*self.debt[s] < 0:
                self.debt[i] += self.debt[s]
                res = m..(res, self.dfs(s+1, cnt+1))
                self.debt[i] -= self.debt[s]
                prev = self.debt[i]
        r.. res __ res != float('inf') ____ cnt
    
    ___ test(self):
        testCases = [
            [[0,1,10], [2,0,5]], # 2
            [[0,1,10], [1,0,1], [1,2,5], [2,0,5]], # 1
        ]
        ___ transactions __ testCases:
            print('transactions: %s' % transactions)
            result = self.minTransfers(transactions)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
