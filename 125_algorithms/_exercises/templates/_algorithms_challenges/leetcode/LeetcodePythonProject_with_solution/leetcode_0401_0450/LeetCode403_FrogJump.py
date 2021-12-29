'''
Created on Apr 9, 2017

@author: MT
'''

class Solution(object):
    ___ canCross(self, stones):
        __ n.. stones: r.. False
        hashmap = {}
        ___ stone __ stones:
            hashmap[stone] = set()
        hashmap[0] = set([1])
        ___ stone __ stones:
            ___ step __ hashmap[stone]:
                reach = step+stone
                __ reach __ stones[-1]:
                    r.. True
                __ reach __ hashmap:
                    hashmap[reach].add(step)
                    __ step > 1:
                        hashmap[reach].add(step-1)
                    hashmap[reach].add(step+1)
        r.. False
    
    ___ test(self):
        testCases = [
            [0,1,3,5,6,8,12,17], # True
            [0,1,2,3,4,8,9,11], # False
        ]
        ___ stones __ testCases:
            print('stones: %s' % stones)
            result= self.canCross(stones)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
