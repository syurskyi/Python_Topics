'''
Created on Mar 26, 2019

@author: tongq
'''
class Solution(object):
    ___ isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        w = W
        __ len(hand) % w != 0:
            return False
        hashmap = {}
        for num in hand:
            hashmap[num] = hashmap[num]+1 __ num in hashmap else 1
        while hashmap:
            minVal = min(hashmap)
            for i in range(w):
                __ minVal + i not in hashmap:
                    return False
                hashmap[minVal+i] -= 1
                __ hashmap[minVal+i] == 0:
                    del hashmap[minVal+i]
        return len(hashmap) == 0
    
    ___ test(self):
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

__ __name__ == '__main__':
    Solution().test()
