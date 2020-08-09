'''
Created on Mar 17, 2017

@author: MT
'''

class Solution(object
    ___ generateAbbreviations(self, word
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.helper(word, 0, 0, '', res)
        r_ res
    
    ___ helper(self, word, i, count, curr, res
        __ i __ le.(word
            __ count:
                curr += str(count)
            res.append(curr)
            r_
        self.helper(word, i+1, count+1, curr, res)
        __ count:
            self.helper(word, i+1, 0, curr+str(count)+word[i], res)
        ____
            self.helper(word, i+1, 0, curr+word[i], res)
    
    ___ test(self
        testCases = [
            'word',
        ]
        for word in testCases:
            print('word: %s' % (word))
            result = self.generateAbbreviations(word)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()

