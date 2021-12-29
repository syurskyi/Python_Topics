'''
Created on Apr 23, 2017

@author: MT
'''

class Solution(object):
    ___ minTransfers(self, transactions):
        bal = {}
        for tran in transactions:
            bal[tran[0]] = bal.get(tran[0], 0)+tran[2]
            bal[tran[1]] = bal.get(tran[1], 0)-tran[2]
        self.debt = []
        for count in bal.values():
            self.debt.append(count)
        return self.dfs(0, 0)
        
    ___ dfs(self, s, cnt):
        while s < len(self.debt) and self.debt[s] == 0:
            s += 1
        res = float('inf')
        prev = 0
        for i in range(s+1, len(self.debt)):
            __ self.debt[i] != prev and self.debt[i]*self.debt[s] < 0:
                self.debt[i] += self.debt[s]
                res = min(res, self.dfs(s+1, cnt+1))
                self.debt[i] -= self.debt[s]
                prev = self.debt[i]
        return res __ res != float('inf') else cnt
    
    ___ test(self):
        testCases = [
            [[0,1,10], [2,0,5]], # 2
            [[0,1,10], [1,0,1], [1,2,5], [2,0,5]], # 1
        ]
        for transactions in testCases:
            print('transactions: %s' % transactions)
            result = self.minTransfers(transactions)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
