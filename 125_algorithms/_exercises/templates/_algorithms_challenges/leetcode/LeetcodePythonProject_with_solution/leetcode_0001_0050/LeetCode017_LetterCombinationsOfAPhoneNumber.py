'''
Created on Jan 10, 2017

@author: MT
'''

class Solution(object):
    ___ letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letMap = {
            0: list(),
            1: list(),
            2: list('abc'),
            3: list('def'),
            4: list('ghi'),
            5: list('jkl'),
            6: list('mno'),
            7: list('pqrs'),
            8: list('tuv'),
            9: list('wxyz'),
        }
        l = []
        for d in digits:
            d = int(d)
            __ d not in (0, 1):
                l.append(letMap[d])
        __ not l: return []
        elem = ''
        result = []
        self.dfs(l, 0, elem, result)
        return result
    
    ___ dfs(self, l, ind, elem, result):
        __ len(elem) == len(l):
            result.append(str(elem))
            return result
        for c in l[ind]:
            elem += c
            self.dfs(l, ind+1, elem, result)
            elem = elem[:-1]
    
    ___ test(self):
        testCases = [
            '',
            '001',
            '2',
            '23',
            '239',
        ]
        
        for digits in testCases:
            print('digits: %s' % (digits))
            result = self.letterCombinations(digits)
            print('result: %s' % (result))
            print('-+'*15+'-')

__ __name__ == '__main__':
    Solution().test()