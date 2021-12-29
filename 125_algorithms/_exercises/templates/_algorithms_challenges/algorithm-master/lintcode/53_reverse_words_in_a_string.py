class Solution:
    """
    @param: s: A string
    @return: A string
    """
    ___ reverseWords(self, s):
        s = s.strip()
        __ not s:
            return ''

        return ' '.join(reversed(s.split()))
