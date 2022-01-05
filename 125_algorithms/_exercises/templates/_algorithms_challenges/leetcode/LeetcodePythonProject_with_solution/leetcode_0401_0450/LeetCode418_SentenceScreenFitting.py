'''
Created on Apr 12, 2017

@author: MT
'''

c_ Solution(object):
    ___ wordsTyping  sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        length = l..(sentence)
        times = [0]*length
        nextInd = [0]*length
        ___ i __ r..(length):
            ind = i
            curLen = 0
            time = 0
            w.... curLen+l..(sentence[ind])<=cols:
                curLen += l..(sentence[ind])+1
                ind += 1
                __ ind __ l..(sentence):
                    ind = 0
                    time += 1
            nextInd[i] = ind
            times[i] = time
        ind = 0
        res = 0
        ___ _ __ r..(rows):
            res += times[ind]
            ind = nextInd[ind]
        r.. res
    
    ___ test
        testCases = [
            (["hello", "world"], 2, 8),
            (["a", "bcd", "e"], 3, 6),
            (["I", "had", "apple", "pie"], 4, 5),
        ]
        ___ sentence, rows, cols __ testCases:
            print('sentence: %s' % sentence)
            print('rows: %s' % rows)
            print('cols: %s' % cols)
            result = wordsTyping(sentence, rows, cols)
            print('result: %s' % result)
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
