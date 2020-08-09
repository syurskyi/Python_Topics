'''
Created on Apr 9, 2017

@author: MT
'''

class Solution(object
    ___ canCross(self, stones
        __ not stones: r_ False
        hashmap = {}
        for stone in stones:
            hashmap[stone] = set()
        hashmap[0] = set([1])
        for stone in stones:
            for step in hashmap[stone]:
                reach = step+stone
                __ reach __ stones[-1]:
                    r_ True
                __ reach in hashmap:
                    hashmap[reach].add(step)
                    __ step > 1:
                        hashmap[reach].add(step-1)
                    hashmap[reach].add(step+1)
        r_ False
    
    ___ test(self
        testCases = [
            [0,1,3,5,6,8,12,17], # True
            [0,1,2,3,4,8,9,11], # False
        ]
        for stones in testCases:
            print('stones: %s' % stones)
            result= self.canCross(stones)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
