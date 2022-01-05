'''
Created on May 5, 2018

@author: tongq
'''
c_ Solution(object):
    ___ toGoatLatin  S):
        """
        :type S: str
        :rtype: str
        """
        s = S
        vowels = set(l..('aeiouAEIOU'))
        arr = s.s..(' ')
        res = ''
        ___ i __ r..(l..(arr)):
            __ n.. arr[i]:
                _____
            word = arr[i]
            __ word[0] n.. __ vowels:
                word = word[1:]+word[0]
            word += 'ma'
            word += 'a'*(i+1)
            res += ' ' + word
        r.. res[1:]
    
    ___ test
        testCases = [
            'I speak Goat Latin',
            'The quick brown fox jumped over the lazy dog',
        ]
        ___ s __ testCases:
            print('s: %s' % s)
            result = toGoatLatin(s)
            print('result: %s' % result)
            print('-='*30+'-')

__ _____ __ _____
    Solution().test()
