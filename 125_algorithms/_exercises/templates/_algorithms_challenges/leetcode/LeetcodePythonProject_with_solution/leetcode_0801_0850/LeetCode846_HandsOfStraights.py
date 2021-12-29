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
        __ l..(hand) % w != 0:
            r.. False
        hashmap = {}
        ___ num __ hand:
            hashmap[num] = hashmap[num]+1 __ num __ hashmap ____ 1
        while hashmap:
            minVal = m..(hashmap)
            ___ i __ r..(w):
                __ minVal + i n.. __ hashmap:
                    r.. False
                hashmap[minVal+i] -= 1
                __ hashmap[minVal+i] __ 0:
                    del hashmap[minVal+i]
        r.. l..(hashmap) __ 0
    
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
        ___ hand, w __ testCases:
            result = self.isNStraightHand(hand, w)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
