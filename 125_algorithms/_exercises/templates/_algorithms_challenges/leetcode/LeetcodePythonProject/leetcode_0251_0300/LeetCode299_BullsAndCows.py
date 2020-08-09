'''
Created on Mar 9, 2017

@author: MT
'''

class Solution(object
    ___ getHint(self, secret, guess
        bulls = set()
        hashmap = {}
        for i, (c1, c2) in enumerate(zip(secret, guess)):
            __ c1 __ c2:
                bulls.add(i)
            ____
                hashmap[c1] = hashmap.get(c1, 0)+1
        cows = 0
        for i, c in enumerate(guess
            __ i not in bulls:
                __ c in hashmap and hashmap[c] > 0:
                    hashmap[c] -= 1
                    cows += 1
        r_ '%sA%sB' % (le.(bulls), cows)
    
    ___ test(self
        testCases = [
            ('1807', '7810'),
            ('1123', '0111'),
        ]
        for secret, guess in testCases:
            print('secret: %s' % (secret))
            print('guess: %s' % (guess))
            result = self.getHint(secret, guess)
            print('result: %s' % (result))
            print('-='*20+'-')

__ __name__ __ '__main__':
    Solution().test()
