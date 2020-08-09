class Solution:
    ___ findHash(self,s
        r_ ''.join(sorted(s))
    ___ groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        ___ s __ strs:
            hashed = self.findHash(s)
            __(hashed not __ m
                m[hashed] = []
            m[hashed].append(s)
        
        ___ p __ m.values(
            answers.append(p)
        
        r_ answers

