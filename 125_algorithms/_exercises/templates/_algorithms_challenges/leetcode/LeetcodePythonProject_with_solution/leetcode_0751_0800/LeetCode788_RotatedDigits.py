'''
Created on Apr 12, 2018

@author: tongq
'''
c_ Solution(o..
    ___ rotatedDigits  N
        """
        :type N: int
        :rtype: int
        """
        cnt = 0
        ___ num __ r..(1, N+1
            __ checkNum(num
                cnt += 1
        r.. cnt
    
    ___ checkNum  num
        arr = l..(s..(num
        i, j = 0, l..(arr)-1
        arr0 = ['']*l..(arr)
        hashmap = {
            '1':'1',
            '2':'5',
            '5':'2',
            '6':'9',
            '8':'8',
            '9':'6',
            '0':'0',
        }
        w.... i <= j:
            __ arr[i] __ hashmap a.. arr[j] __ hashmap:
                arr0[i], arr0[j] = hashmap[arr[i]], hashmap[arr[j]]
                i += 1
                j -= 1
            ____
                r.. F..
        r.. arr0 != arr
    
    ___ test
        testCases = [
            10,
            100,
            857,
        ]
        ___ n __ testCases:
            print('n: %s' % n)
            result = rotatedDigits(n)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
