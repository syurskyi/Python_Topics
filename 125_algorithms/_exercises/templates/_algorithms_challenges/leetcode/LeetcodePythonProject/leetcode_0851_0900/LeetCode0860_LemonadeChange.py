'''
Created on Sep 15, 2019

@author: tongq
'''
class Solution(object
    ___ lemonadeChange(self, bills
        """
        :type bills: List[int]
        :rtype: bool
        """
        hashmap = {
            5:0,
            10:0,
            20:0,
        }
        ___ b in bills:
            __ b __ 10:
                __ hashmap[5] >= 1:
                    hashmap[5] -= 1
                ____
                    r_ False
            ____ b __ 20:
                val = 20
                __ hashmap[10] >= 1:
                    hashmap[10] -= 1
                    val -= 10
                __ val __ 10:
                    __ hashmap[5] >= 1:
                        hashmap[5] -= 1
                    ____
                        r_ False
                ____
                    __ hashmap[5] >= 3:
                        hashmap[5] -= 3
                    ____
                        r_ False
            hashmap[b] += 1
        r_ True
    
    ___ test(self
        testCases = [
#             [5,5,5,10,20],
            [5, 5, 10, 10, 20],
        ]
        ___ bills in testCases:
            res = self.lemonadeChange(bills)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
