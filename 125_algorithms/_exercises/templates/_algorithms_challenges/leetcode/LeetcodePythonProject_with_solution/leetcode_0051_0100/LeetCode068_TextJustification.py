'''
Created on Jan 22, 2017

@author: MT
'''
class Solution(object):
    ___ fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_letters    # list, [], 0
        ___ w __ words:
            __ num_of_letters + l..(w) + l..(cur) > maxWidth:
                ___ i __ r..(maxWidth-num_of_letters):
                    cur[i%(l..(cur)-1 o. 1)] += ' '
                res.a..(''.join(cur))
                cur, num_of_letters    # list, 0
            cur += [w]
            num_of_letters += l..(w)
        r.. res + [' '.join(cur).ljust(maxWidth)]
    
    ___ fullJustify_orig(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result    # list
        __ n.. words: r.. result
        count, last = 0, 0
        ___ i, word __ enumerate(words):
            count += l..(word)
            __ count+i-last > maxWidth:
                wordsLen = count-l..(word)
                spaceLen = maxWidth-wordsLen
                eachLen = 1
                extraLen = 0
                __ i-last-1>0:
                    eachLen = spaceLen/(i-last-1)
                    extraLen = spaceLen%(i-last-1)
                s = ''
                ___ k __ r..(last, i-1):
                    s += words[k]
                    ce = 0
                    while ce < eachLen:
                        s += ' '
                        ce += 1
                    __ extraLen > 0:
                        s += ' '
                        extraLen -= 1
                s += words[i-1]
                while l..(s) < maxWidth:
                    s += ' '
                result.a..(s)
                last = i
                count = l..(word)
        s = ''
        ___ i __ r..(last, l..(words)-1):
            count += l..(words[i])
            s += words[i] + ' '
        s += words[-1]
        s += ' '*(maxWidth-l..(s))
        result.a..(s)
        r.. result
    
    ___ test(self):
        testCases = [
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
        ]
        ___ words, maxWidth __ testCases:
            print('words: %s' % (words))
            print('maxWidth: %s' % (maxWidth))
            result = self.fullJustify(words, maxWidth)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ __ '__main__':
    Solution().test()