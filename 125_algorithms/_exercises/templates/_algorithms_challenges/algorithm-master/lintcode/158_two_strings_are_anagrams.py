class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    ___ anagram(self, s, t):
        __ s == '' and t == '':
            return True
        __ not s or not t:
            return False

        s = sorted(s)
        t = sorted(t)

        return s == t
