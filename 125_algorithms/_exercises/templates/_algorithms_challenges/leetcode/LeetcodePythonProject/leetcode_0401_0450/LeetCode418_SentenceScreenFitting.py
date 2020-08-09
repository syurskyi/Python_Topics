'''
Created on Apr 12, 2017

@author: MT
'''

class Solution(object
    ___ wordsTyping(self, sentence, rows, cols
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        length = le.(sentence)
        times = [0]*length
        nextInd = [0]*length
        ___ i in range(length
            ind = i
            curLen = 0
            time = 0
            w___ curLen+le.(sentence[ind])<=cols:
                curLen += le.(sentence[ind])+1
                ind += 1
                __ ind __ le.(sentence
                    ind = 0
                    time += 1
            nextInd[i] = ind
            times[i] = time
        ind = 0
        res = 0
        ___ _ in range(rows
            res += times[ind]
            ind = nextInd[ind]
        r_ res
    
    ___ test(self
        testCases = [
            (["hello", "world"], 2, 8),
            (["a", "bcd", "e"], 3, 6),
            (["I", "had", "apple", "pie"], 4, 5),
        ]
        ___ sentence, rows, cols in testCases:
            print('sentence: %s' % sentence)
            print('rows: %s' % rows)
            print('cols: %s' % cols)
            result = self.wordsTyping(sentence, rows, cols)
            print('result: %s' % result)
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
