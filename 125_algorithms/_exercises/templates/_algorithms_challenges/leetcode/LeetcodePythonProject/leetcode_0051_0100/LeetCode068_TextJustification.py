'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object
    ___ fullJustify(self, words, maxWidth
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters = [], [], 0
        ___ w in words:
            __ num_of_letters + le.(w) + le.(cur) > maxWidth:
                ___ i in range(maxWidth-num_of_letters
                    cur[i%(le.(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += le.(w)
        r_ res + [' '.join(cur).ljust(maxWidth)]
    
    ___ fullJustify_orig(self, words, maxWidth
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        __ not words: r_ result
        count, last = 0, 0
        ___ i, word in enumerate(words
            count += le.(word)
            __ count+i-last > maxWidth:
                wordsLen = count-le.(word)
                spaceLen = maxWidth-wordsLen
                eachLen = 1
                extraLen = 0
                __ i-last-1>0:
                    eachLen = spaceLen/(i-last-1)
                    extraLen = spaceLen%(i-last-1)
                s = ''
                ___ k in range(last, i-1
                    s += words[k]
                    ce = 0
                    w___ ce < eachLen:
                        s += ' '
                        ce += 1
                    __ extraLen > 0:
                        s += ' '
                        extraLen -= 1
                s += words[i-1]
                w___ le.(s) < maxWidth:
                    s += ' '
                result.append(s)
                last = i
                count = le.(word)
        s = ''
        ___ i in range(last, le.(words)-1
            count += le.(words[i])
            s += words[i] + ' '
        s += words[-1]
        s += ' '*(maxWidth-le.(s))
        result.append(s)
        r_ result
    
    ___ test(self
        testCases = [
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
        ]
        ___ words, maxWidth in testCases:
            print('words: %s' % (words))
            print('maxWidth: %s' % (maxWidth))
            result = self.fullJustify(words, maxWidth)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()