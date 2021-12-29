'''
Created on Apr 16, 2018

@author: tongq
'''
class Solution(object):
    ___ numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        hashmap = {}
        ___ i __ r..(26):
            c = chr(ord('a')+i)
            hashmap[c]    # list
        ___ word __ words:
            hashmap[word[0]].a..(word)
        count = 0
        ___ c __ S:
            deque = hashmap[c]
            size = l..(deque)
            ___ i __ r..(size):
                word = deque.pop(0)
                __ l..(word) __ 1:
                    count += 1
                ____:
                    hashmap[word[1]].a..(word[1:])
        r.. count
    
    ___ test(self):
        testCases = [
            [
                'abcde',
                ["a", "bb", "acd", "ace"],
            ],
        ]
        ___ s, words __ testCases:
            result = self.numMatchingSubseq(s, words)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
