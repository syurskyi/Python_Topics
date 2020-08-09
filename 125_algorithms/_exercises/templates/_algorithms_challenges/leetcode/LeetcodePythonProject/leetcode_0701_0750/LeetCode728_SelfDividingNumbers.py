'''
Created on Mar 4, 2018

@author: tongq
'''
class Solution(object
    ___ selfDividingNumbers(self, left, right
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        ___ num in range(left, right+1
            __ self.isSelfDividing(num
                res.append(num)
        r_ res
        
    ___ isSelfDividing(self, num
        ___ digit in str(num
            d = int(digit)
            __ d __ 0 or num%d != 0:
                r_ False
        r_ True
    
    ___ test(self
        testCases = [
            [1, 22],
        ]
        ___ left, right in testCases:
            print('left: %s' % left)
            print('right: %s' % right)
            result = self.selfDividingNumbers(left, right)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
