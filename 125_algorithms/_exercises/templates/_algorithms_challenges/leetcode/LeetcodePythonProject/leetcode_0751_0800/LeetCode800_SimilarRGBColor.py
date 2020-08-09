'''
Created on Apr 19, 2018

@author: tongq
'''
class Solution(object
    ___ similarRGB(self, color
        """
        :type color: str
        :rtype: str
        """
        r, g, b = color[1:3].lower(), color[3:5].lower(), color[5:7].lower()
        print(r, g, b)
        r_ '#' + self.getTwoDigits(r) + self.getTwoDigits(g) + self.getTwoDigits(b)
    
    ___ getTwoDigits(self, s
        res = 0
        diff = float('inf')
        ___ s0 in ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99',\
                   'aa', 'bb', 'cc', 'dd', 'ee', 'ff']:
            num0 = self.convert(s0)
            num = self.convert(s)
            diff0 = (num0-num)**2
            __ diff0 < diff:
                res = s0
                diff = diff0
        r_ res
    
    ___ convert(self, s
        num = 16*(ord(s[0])-ord('0') __ s[0].isdigit() else ord(s[0])-ord('a')+10)
        num += (ord(s[1])-ord('0') __ s[1].isdigit() else ord(s[1])-ord('a')+10)
        r_ num
    
    ___ test(self
        testCases = [
            '#09f166',
        ]
        ___ color in testCases:
            print('color: %s' % color)
            result = self.similarRGB(color)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
