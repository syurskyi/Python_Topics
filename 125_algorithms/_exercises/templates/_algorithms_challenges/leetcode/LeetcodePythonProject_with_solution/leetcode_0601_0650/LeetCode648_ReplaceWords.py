'''
Created on Oct 2, 2017

@author: MT
'''
class Solution(object):
    ___ replaceWords(self, d.., sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        d...sort(key=l.... x: l..(x))
        resArr    # list
        words = sentence.split(' ')
        ___ i, word __ enumerate(words):
            ___ s __ d..:
                __ word[:l..(s)] __ s:
                    resArr.a..(s)
                    break
            __ i+1 > l..(resArr):
                resArr.a..(word)
        r.. ' '.join(resArr)
    
    ___ test(self):
        testCases = [
            [
                ["cat", "bat", "rat"],
                "the cattle was rattled by the battery",
            ],
        ]
        ___ d.., sentence __ testCases:
            print('dict: %s' % d..)
            print('sentence: %s' % sentence)
            result = self.replaceWords(d.., sentence)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
