'''
Created on Apr 10, 2017

@author: MT
'''

c_ Solution(object):
    ___ validWordAbbreviation(self, word, abbr):
        i, j = 0, 0
        w.... i < l..(word) a.. j < l..(abbr):
            __ abbr[j].isdigit():
                prev = j
                w.... j+1 < l..(abbr) a.. abbr[j+1].isdigit():
                    j+=1
                __ abbr[prev:j+1].startswith('0'): r.. F..
                num = int(abbr[prev:j+1])
                i += num
                j += 1
            ____:
                __ word[i] != abbr[j]:
                    r.. F..
                i+=1
                j+=1
        __ i != l..(word) o. j != l..(abbr):
            r.. F..
        r.. T..
    
    ___ test
        testCases = [
            ('internationalization', 'i12iz4n'),
            ('apple', 'a2e'),
        ]
        ___ word, abbr __ testCases:
            print('word: %s' % word)
            print('abbr: %s' % abbr)
            result = validWordAbbreviation(word, abbr)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
