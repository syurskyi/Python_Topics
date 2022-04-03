'''
Created on Apr 23, 2017

@author: MT
'''

c_ Solution(o..
    ___ minTransfers  transactions
        bal    # dict
        ___ tran __ transactions:
            bal[tran[0]] = bal.g.. tran[0], 0)+tran[2]
            bal[tran[1]] = bal.g.. tran[1], 0)-tran[2]
        debt    # list
        ___ count __ bal.v..
            debt.a..(count)
        r.. dfs(0, 0)
        
    ___ dfs  s, cnt
        w.... s < l..(debt) a.. debt[s] __ 0:
            s += 1
        res = f__('inf')
        prev = 0
        ___ i __ r..(s+1, l..(debt)):
            __ debt[i] != prev a.. debt[i]*debt[s] < 0:
                debt[i] += debt[s]
                res = m..(res, dfs(s+1, cnt+1))
                debt[i] -= debt[s]
                prev = debt[i]
        r.. res __ res != f__('inf') ____ cnt
    
    ___ test
        testCases = [
            [[0,1,10], [2,0,5]], # 2
            [[0,1,10], [1,0,1], [1,2,5], [2,0,5]], # 1
        ]
        ___ transactions __ testCases:
            print('transactions: %s' % transactions)
            result = minTransfers(transactions)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
