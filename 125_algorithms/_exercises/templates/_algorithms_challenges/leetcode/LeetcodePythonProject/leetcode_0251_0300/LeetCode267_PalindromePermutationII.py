'''
Created on Mar 4, 2017

@author: MT
'''

class Solution(object
    ___ generatePalindromes(self, s
        """
        :type s: str
        :rtype: List[str]
        """
        __ not s: r_ False
        hashmap = {}
        for c in s:
            hashmap[c] = hashmap.get(c, 0)+1
        odd = 0
        oddVal = ''
        for key, value in hashmap.items(
            __ value%2 != 0:
                oddVal = key
                odd += 1
        __ le.(s)%2 __ 0:
            __ odd != 0:
                r_ []
        ____
            __ odd >= 2:
                r_ []
        result = []
        self.helper(oddVal, le.(s), hashmap, result)
        r_ result
    
    ___ helper(self, s0, length, hashmap, result
        __ le.(s0) >= length:
            result.append(s0)
            r_
        for c, val in hashmap.items(
            __ val >= 2:
                hashmap[c] -= 2
                self.helper(c+s0+c, length, hashmap, result)
                hashmap[c] += 2
    
    ___ test(self
        testCases = [
            'aaabb',
            'abc',
            'aab',
        ]
        for s in testCases:
            print('s: %s' % (s))
            result = self.generatePalindromes(s)
            print('result: %s' % (result))
            print('-='*20+'-')
            

__ __name__ __ '__main__':
    Solution().test()
