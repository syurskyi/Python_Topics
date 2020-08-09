class Solution:
    ___ findHash(self,s
        r_ ''.join(sorted(s))
    ___ groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answers = []
        m = {}

        for s in strs:
            hashed = self.findHash(s)
            __(hashed not in m
                m[hashed] = []
            m[hashed].append(s)
        
        for p in m.values(
            answers.append(p)
        
        r_ answers

