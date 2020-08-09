'''
Created on Mar 26, 2019

@author: tongq
'''
class Solution(object
    ___ isNStraightHand(self, hand, W
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        w = W
        __ le.(hand) % w != 0:
            r_ False
        hashmap = {}
        for num in hand:
            hashmap[num] = hashmap[num]+1 __ num in hashmap else 1
        w___ hashmap:
            minVal = min(hashmap)
            for i in range(w
                __ minVal + i not in hashmap:
                    r_ False
                hashmap[minVal+i] -= 1
                __ hashmap[minVal+i] __ 0:
                    del hashmap[minVal+i]
        r_ le.(hashmap) __ 0
    
    ___ test(self
        testCases = [
            [
                [1,2,3,6,2,3,4,7,8],
                3,
            ],
            [
                [1,2,3,4,5],
                4,
            ],
        ]
        for hand, w in testCases:
            result = self.isNStraightHand(hand, w)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
