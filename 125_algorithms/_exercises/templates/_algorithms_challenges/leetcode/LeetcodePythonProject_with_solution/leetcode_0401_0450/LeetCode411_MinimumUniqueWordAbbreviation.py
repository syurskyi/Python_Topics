'''
Created on Apr 11, 2017

@author: MT
'''

class Solution(object):
    ___ minAbbreviation(self, target, dictionary):
        diffs = []
        m = len(target)
        for word in dictionary:
            __ len(word) != m: continue
            bits = 0
            for i, c in enumerate(word):
                __ c != target[i]:
                    bits += 2**i
            diffs.append(bits)
        __ not diffs:
            return str(m)
        abbrs = []
        for i in range(2**m):
            __ all(d&i for d in diffs):
                abbrs.append(self.abbr(target, i))
        return min(abbrs, key=lambda x: len(x))
    
    ___ abbr(self, target, num):
        word, count = '', 0
        for w in target:
            __ num & 1 == 1:
                __ count:
                    word += str(count)
                    count = 0
                word += w
            else:
                count += 1
            num >>= 1
        __ count:
            word += str(count)
        return word
    
    ___ test(self):
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
        for target, dictionary in testCases:
            print('target: %s' % target)
            print('dictionary: %s' % dictionary)
            result = self.minAbbreviation(target, dictionary)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
