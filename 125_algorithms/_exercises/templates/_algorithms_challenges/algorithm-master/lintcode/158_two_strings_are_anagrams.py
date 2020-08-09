class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    ___ anagram(self, s, t
        __ s __ '' and t __ '':
            r_ True
        __ not s or not t:
            r_ False

        s = sorted(s)
        t = sorted(t)

        r_ s __ t
