c_ Solution:
    ___ findHash(,s
        r_ ''.join(sorted(s))
    ___ groupAnagrams(, strs: L..[str]) -> L..[L..[str]]:
        answers _ []
        m _ {}

        ___ s __ strs:
            hashed _ .findHash(s)
            __(hashed no. __ m
                m[hashed] _ []
            m[hashed].append(s)
        
        ___ p __ m.values(
            answers.append(p)
        
        r_ answers

