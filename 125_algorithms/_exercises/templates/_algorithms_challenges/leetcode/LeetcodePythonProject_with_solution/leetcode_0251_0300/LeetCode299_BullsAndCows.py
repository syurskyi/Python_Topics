'''
Created on Mar 9, 2017

@author: MT
'''

c_ Solution(object):
    ___ getHint(self, secret, guess):
        bulls = set()
        hashmap    # dict
        ___ i, (c1, c2) __ e..(z..(secret, guess)):
            __ c1 __ c2:
                bulls.add(i)
            ____:
                hashmap[c1] = hashmap.get(c1, 0)+1
        cows = 0
        ___ i, c __ e..(guess):
            __ i n.. __ bulls:
                __ c __ hashmap a.. hashmap[c] > 0:
                    hashmap[c] -= 1
                    cows += 1
        r.. '%sA%sB' % (l..(bulls), cows)
    
    ___ test
        testCases = [
            ('1807', '7810'),
            ('1123', '0111'),
        ]
        ___ secret, guess __ testCases:
            print('secret: %s' % (secret))
            print('guess: %s' % (guess))
            result = getHint(secret, guess)
            print('result: %s' % (result))
            print('-='*20+'-')

__ _____ __ _____
    Solution().test()
