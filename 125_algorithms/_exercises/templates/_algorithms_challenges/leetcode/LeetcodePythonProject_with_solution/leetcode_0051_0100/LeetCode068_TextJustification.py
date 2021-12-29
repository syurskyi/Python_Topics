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
        res, cur, num_of_letters = [], [], 0
        for w in words:
            __ num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth-num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
    
    ___ fullJustify_orig(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        __ not words: return result
        count, last = 0, 0
        for i, word in enumerate(words):
            count += len(word)
            __ count+i-last > maxWidth:
                wordsLen = count-len(word)
                spaceLen = maxWidth-wordsLen
                eachLen = 1
                extraLen = 0
                __ i-last-1>0:
                    eachLen = spaceLen/(i-last-1)
                    extraLen = spaceLen%(i-last-1)
                s = ''
                for k in range(last, i-1):
                    s += words[k]
                    ce = 0
                    while ce < eachLen:
                        s += ' '
                        ce += 1
                    __ extraLen > 0:
                        s += ' '
                        extraLen -= 1
                s += words[i-1]
                while len(s) < maxWidth:
                    s += ' '
                result.append(s)
                last = i
                count = len(word)
        s = ''
        for i in range(last, len(words)-1):
            count += len(words[i])
            s += words[i] + ' '
        s += words[-1]
        s += ' '*(maxWidth-len(s))
        result.append(s)
        return result
    
    ___ test(self):
        testCases = [
            (["This", "is", "an", "example", "of", "text", "justification."], 16),
        ]
        for words, maxWidth in testCases:
            print('words: %s' % (words))
            print('maxWidth: %s' % (maxWidth))
            result = self.fullJustify(words, maxWidth)
            print('result: %s' % (result))
            print('-='*15+'-')

__ __name__ == '__main__':
    Solution().test()