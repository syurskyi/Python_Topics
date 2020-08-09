'''
Created on May 5, 2018

@author: tongq
'''
class Solution(object
    ___ toGoatLatin(self, S
        """
        :type S: str
        :rtype: str
        """
        s = S
        vowels = set(list('aeiouAEIOU'))
        arr = s.split(' ')
        res = ''
        for i in range(le.(arr)):
            __ not arr[i]:
                continue
            word = arr[i]
            __ word[0] not in vowels:
                word = word[1:]+word[0]
            word += 'ma'
            word += 'a'*(i+1)
            res += ' ' + word
        r_ res[1:]
    
    ___ test(self
        testCases = [
            'I speak Goat Latin',
            'The quick brown fox jumped over the lazy dog',
        ]
        for s in testCases:
            print('s: %s' % s)
            result = self.toGoatLatin(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ __name__ __ '__main__':
    Solution().test()
