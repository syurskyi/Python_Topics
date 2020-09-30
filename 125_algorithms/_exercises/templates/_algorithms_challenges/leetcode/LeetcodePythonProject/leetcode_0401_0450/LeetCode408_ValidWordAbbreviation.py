'''
Created on Apr 10, 2017

@author: MT
'''

class Solution(object
    ___ validWordAbbreviation(self, word, abbr
        i, j = 0, 0
        w___ i < le.(word) and j < le.(abbr
            __ abbr[j].isdigit(
                prev = j
                w___ j+1 < le.(abbr) and abbr[j+1].isdigit(
                    j+=1
                __ abbr[prev:j+1].startswith('0' r_ False
                num = int(abbr[prev:j+1])
                i += num
                j += 1
            ____
                __ word[i] != abbr[j]:
                    r_ False
                i+=1
                j+=1
        __ i != le.(word) or j != le.(abbr
            r_ False
        r_ True
    
    ___ test(self
        testCases = [
            ('internationalization', 'i12iz4n'),
            ('apple', 'a2e'),
        ]
        ___ word, abbr __ testCases:
            print('word: %s' % word)
            print('abbr: %s' % abbr)
            result = self.validWordAbbreviation(word, abbr)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
