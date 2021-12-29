'''
Created on Mar 26, 2018

@author: tongq
'''
class Solution(object):
    ___ ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        x = 0
        ips= ip.split('.')
        ___ ip __ ips:
            x = int(ip) + x*256
        res    # list
        while n > 0:
            step = x &(-x)
            while step > n:
                step /= 2
            res.a..(self.long2ip(x, step))
            x += step
            n -= step
        r.. res
    
    ___ long2ip(self, x, step):
        res = [0]*4
        ___ i __ r..(3, -1, -1):
            res[i] = x&255
            x >>= 8
        n = 33
        while step > 0:
            n -= 1
            step //= 2
        r.. '.'.join([str(s) ___ s __ res])+'/'+str(n)
    
    ___ test(self):
        testCases = [
            [
                '255.0.0.7',
                10,
            ],
        ]
        ___ ip, n __ testCases:
            result = self.ipToCIDR(ip, n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
    
    ___ n __ r..(1, 20):
        print('n: %s' % n)
        print('{:b}'.format(n))
        print('{:b}'.format(-n))
        result = n&-n
        print('res: %s' % result)
        print('-='*30+'-')
