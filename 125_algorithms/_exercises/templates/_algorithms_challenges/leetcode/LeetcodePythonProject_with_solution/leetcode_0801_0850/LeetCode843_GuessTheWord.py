'''
Created on Mar 6, 2019

@author: tongq
'''
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """

_______ collections, itertools

class Master(object):
    ___ guess(self, word):
        """
        :type word: str
        :rtype int
        """
        pass

class Solution(object):
    ___ findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            count = collections.Counter(w1 ___ w1, w2 __ itertools.permutations(wordlist, 2) __ self.match(w1, w2) __ 0)
            guess = m..(wordlist, key=l.... w:count[w])
            n = master.guess(guess)
            wordlist = [w ___ w __ wordlist __ self.match(w, guess) __ n]
    
    ___ match(self, w1, w2):
        matches = 0
        ___ c1, c2 __ zip(w1, w2):
            __ c1 __ c2: matches += 1
        r.. matches
    
    ___ test(self):
        testCases = [
            
        ]
        ___ wordlist, master __ testCases:
            result = self.findSecretWord(wordlist, master)
            print('result: %s' % result)

__ __name__ __ '__main__':
    Solution().test()
