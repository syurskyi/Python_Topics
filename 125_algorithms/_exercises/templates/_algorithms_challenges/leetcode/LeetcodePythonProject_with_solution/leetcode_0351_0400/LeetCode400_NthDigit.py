'''
Created on Apr 5, 2017

@author: MT
'''

c_ Solution(object):
    ___ findNthDigit(self, n):
        length, count, start = 1, 9, 1
        w.... n > length*count:
            n -= length*count
            length += 1
            count *= 10
            start *= 10
        start += (n-1)//length
        s = s..(start)
        r.. i..(s[(n-1)%length])
    
    ___ test
        testCases = [
            3,
            11,
            250,
            300,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = findNthDigit(num)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
