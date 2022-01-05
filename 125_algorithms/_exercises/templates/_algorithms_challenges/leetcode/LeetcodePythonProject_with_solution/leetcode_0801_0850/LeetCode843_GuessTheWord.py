'''
Created on Mar 6, 2019

@author: tongq
'''
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

_______ c.., i..

c_ Master(object):
    ___ guess  word):
        """
        :type word: str
        :rtype int
        """
        p..

c_ Solution(object):
    ___ findSecretWord  wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        w.... n < 6:
            count = c...Counter(w1 ___ w1, w2 __ i...permutations(wordlist, 2) __ m..(w1, w2) __ 0)
            guess = m..(wordlist, key=l.... w:count[w])
            n = master.guess(guess)
            wordlist = [w ___ w __ wordlist __ m..(w, guess) __ n]
    
    ___ m..  w1, w2):
        matches = 0
        ___ c1, c2 __ z..(w1, w2):
            __ c1 __ c2: matches += 1
        r.. matches
    
    ___ test
        testCases = [
            
        ]
        ___ wordlist, master __ testCases:
            result = findSecretWord(wordlist, master)
            print('result: %s' % result)

__ _____ __ _____
    Solution().test()
