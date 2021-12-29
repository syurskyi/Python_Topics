'''
Created on Oct 2, 2017

@author: MT
'''
class Solution(object):
    ___ replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict.sort(key=lambda x: len(x))
        resArr = []
        words = sentence.split(' ')
        for i, word in enumerate(words):
            for s in dict:
                __ word[:len(s)] == s:
                    resArr.append(s)
                    break
            __ i+1 > len(resArr):
                resArr.append(word)
        return ' '.join(resArr)
    
    ___ test(self):
        testCases = [
            [
                ["cat", "bat", "rat"],
                "the cattle was rattled by the battery",
            ],
        ]
        for dict, sentence in testCases:
            print('dict: %s' % dict)
            print('sentence: %s' % sentence)
            result = self.replaceWords(dict, sentence)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ == '__main__':
    Solution().test()
