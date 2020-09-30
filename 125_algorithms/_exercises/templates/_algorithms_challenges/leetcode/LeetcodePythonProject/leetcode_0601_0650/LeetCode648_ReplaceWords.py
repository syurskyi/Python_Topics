'''
Created on Oct 2, 2017

@author: MT
'''
class Solution(object
    ___ replaceWords(self, dict, sentence
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict.sort(key=lambda x: le.(x))
        resArr =   # list
        words = sentence.split(' ')
        ___ i, word __ enumerate(words
            ___ s __ dict:
                __ word[:le.(s)] __ s:
                    resArr.append(s)
                    break
            __ i+1 > le.(resArr
                resArr.append(word)
        r_ ' '.join(resArr)
    
    ___ test(self
        testCases = [
            [
                ["cat", "bat", "rat"],
                "the cattle was rattled by the battery",
            ],
        ]
        ___ dict, sentence __ testCases:
            print('dict: %s' % dict)
            print('sentence: %s' % sentence)
            result = self.replaceWords(dict, sentence)
            print('result: %s' % result)
            print('-='*30+'-')

__  -n __ '__main__':
    Solution().test()
