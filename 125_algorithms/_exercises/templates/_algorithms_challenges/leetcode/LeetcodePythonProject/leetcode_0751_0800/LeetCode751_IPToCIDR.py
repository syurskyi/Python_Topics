'''
Created on Mar 26, 2018

@author: tongq
'''
class Solution(object
    ___ ipToCIDR(self, ip, n
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        x = 0
        ips= ip.split('.')
        ___ ip in ips:
            x = int(ip) + x*256
        res = []
        w___ n > 0:
            step = x &(-x)
            w___ step > n:
                step /= 2
            res.append(self.long2ip(x, step))
            x += step
            n -= step
        r_ res
    
    ___ long2ip(self, x, step
        res = [0]*4
        ___ i in range(3, -1, -1
            res[i] = x&255
            x >>= 8
        n = 33
        w___ step > 0:
            n -= 1
            step //= 2
        r_ '.'.join([str(s) ___ s in res])+'/'+str(n)
    
    ___ test(self
        testCases = [
            [
                '255.0.0.7',
                10,
            ],
        ]
        ___ ip, n in testCases:
            result = self.ipToCIDR(ip, n)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
    
    ___ n in range(1, 20
        print('n: %s' % n)
        print('{:b}'.format(n))
        print('{:b}'.format(-n))
        result = n&-n
        print('res: %s' % result)
        print('-='*30+'-')
