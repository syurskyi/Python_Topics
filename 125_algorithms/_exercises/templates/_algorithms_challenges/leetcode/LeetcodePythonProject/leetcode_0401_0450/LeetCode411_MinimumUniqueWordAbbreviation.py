'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object
    ___ minAbbreviation(self, target, dictionary
        diffs =   # list
        m = le.(target)
        ___ word __ dictionary:
            __ le.(word) != m: continue
            bits = 0
            ___ i, c __ enumerate(word
                __ c != target[i]:
                    bits += 2**i
            diffs.append(bits)
        __ not diffs:
            r_ str(m)
        abbrs =   # list
        ___ i __ range(2**m
            __ al.(d&i ___ d __ diffs
                abbrs.append(self.abbr(target, i))
        r_ min(abbrs, key=lambda x: le.(x))
    
    ___ abbr(self, target, num
        word, count = '', 0
        ___ w __ target:
            __ num & 1 __ 1:
                __ count:
                    word += str(count)
                    count = 0
                word += w
            ____
                count += 1
            num >>= 1
        __ count:
            word += str(count)
        r_ word
    
    ___ test(self
        testCases = [
            [
                "apple",
                ["blade"],
            ],
            [
                "apple",
                ["plain", "amber", "blade"],
            ],
        ]
        ___ target, dictionary __ testCases:
            print('target: %s' % target)
            print('dictionary: %s' % dictionary)
            result = self.minAbbreviation(target, dictionary)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
