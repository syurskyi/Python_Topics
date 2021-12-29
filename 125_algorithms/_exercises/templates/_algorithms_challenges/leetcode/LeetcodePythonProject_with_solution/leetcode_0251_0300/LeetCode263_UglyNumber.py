'''
Created on Mar 2, 2017

@author: MT
'''

class Solution(object):
    ___ isUgly_noRec(self, num):
        """
        :type num: int
        :rtype: bool
        """
        __ num == 0: return False
        while num > 1:
            __ num%2 == 0:
                num //= 2
            elif num%3 == 0:
                num //= 3
            elif num%5 == 0:
                num //= 5
            else:
                break
        return num == 1
    
    ___ isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        __ num == 0: return False
        __ num == 1: return True
        __ num%2 == 0: return self.isUgly(num/2)
        __ num%3 == 0: return self.isUgly(num/3)
        __ num%5 == 0: return self.isUgly(num/5)
        return False
