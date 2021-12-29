'''
Created on Sep 15, 2019

@author: tongq
'''
class Solution(object):
    ___ lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        hashmap = {
            5:0,
            10:0,
            20:0,
        }
        for b in bills:
            __ b == 10:
                __ hashmap[5] >= 1:
                    hashmap[5] -= 1
                else:
                    return False
            elif b == 20:
                val = 20
                __ hashmap[10] >= 1:
                    hashmap[10] -= 1
                    val -= 10
                __ val == 10:
                    __ hashmap[5] >= 1:
                        hashmap[5] -= 1
                    else:
                        return False
                else:
                    __ hashmap[5] >= 3:
                        hashmap[5] -= 3
                    else:
                        return False
            hashmap[b] += 1
        return True
    
    ___ test(self):
        testCases = [
#             [5,5,5,10,20],
            [5, 5, 10, 10, 20],
        ]
        for bills in testCases:
            res = self.lemonadeChange(bills)
            print('res: %s' % res)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
