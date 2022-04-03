'''
Created on Oct 12, 2017

@author: MT
'''
c_ Solution(o..
    ___ maximumSwap  num
        """
        :type num: int
        :rtype: int
        """
        arr = l..(s..(num))
        hashmap    # dict
        ___ i, c __ e..(arr
            hashmap[c] = i
        flag = F..
        ___ i, c __ e..(arr
            ___ c0 __ '9876543210':
                __ c0 > c a.. hashmap.g.. c0, -1) > i:
                    arr[i], arr[hashmap[c0]] = arr[hashmap[c0]], arr[i]
                    flag = T..
                    _____
            __ flag:
                _____
        r.. i..(''.j..(arr))
    
    ___ test
        testCases = [
            2736,
            9973,
            98368,
        ]
        ___ num __ testCases:
            print('num: %s' % num)
            result = maximumSwap(num)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
