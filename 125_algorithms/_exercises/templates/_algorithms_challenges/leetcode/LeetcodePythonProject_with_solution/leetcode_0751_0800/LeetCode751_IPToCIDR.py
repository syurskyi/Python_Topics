'''
Created on Mar 26, 2018

@author: tongq
'''
c_ Solution(o..
    ___ ipToCIDR  ip, n
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        x = 0
        ips= ip.s..('.')
        ___ ip __ ips:
            x = i..(ip) + x*256
        res    # list
        w.... n > 0:
            step = x &(-x)
            w.... step > n:
                step /= 2
            res.a..(long2ip(x, step
            x += step
            n -= step
        r.. res
    
    ___ long2ip  x, step
        res = [0]*4
        ___ i __ r..(3, -1, -1
            res[i] = x&255
            x >>= 8
        n = 33
        w.... step > 0:
            n -= 1
            step //= 2
        r.. '.'.j..([s..(s) ___ s __ res])+'/'+s..(n)
    
    ___ test
        testCases = [
            [
                '255.0.0.7',
                10,
            ],
        ]
        ___ ip, n __ testCases:
            result = ipToCIDR(ip, n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
    
    ___ n __ r..(1, 20
        print('n: %s' % n)
        print('{:b}'.f..(n
        print('{:b}'.f..(-n
        result = n&-n
        print('res: %s' % result)
        print('-='*30+'-')
