'''
Created on Apr 19, 2018

@author: tongq
'''
c_ Solution(o..):
    ___ similarRGB  color):
        """
        :type color: str
        :rtype: str
        """
        r, g, b = color[1:3].l.., color[3:5].l.., color[5:7].l..
        print(r, g, b)
        r.. '#' + getTwoDigits(r) + getTwoDigits(g) + getTwoDigits(b)
    
    ___ getTwoDigits  s):
        res = 0
        diff = float('inf')
        ___ s0 __ ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99',\
                   'aa', 'bb', 'cc', 'dd', 'ee', 'ff']:
            num0 = convert(s0)
            num = convert(s)
            diff0 = (num0-num)**2
            __ diff0 < diff:
                res = s0
                diff = diff0
        r.. res
    
    ___ convert  s):
        num = 16*(o..(s[0])-o..('0') __ s[0].i.. ____ o..(s[0])-o..('a')+10)
        num += (o..(s[1])-o..('0') __ s[1].i.. ____ o..(s[1])-o..('a')+10)
        r.. num
    
    ___ test
        testCases = [
            '#09f166',
        ]
        ___ color __ testCases:
            print('color: %s' % color)
            result = similarRGB(color)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
