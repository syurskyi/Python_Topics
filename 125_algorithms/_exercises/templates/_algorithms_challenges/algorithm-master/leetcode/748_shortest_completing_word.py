class Solution:
    ___ shortestCompletingWord(self, P, words):
        """
        :type P: str
        :type words: List[str]
        :rtype: str
        """

        ans = ''
        __ n.. P o. n.. words:
            r.. ans

        p_times = self.get_times(P)
        _min_size = float('inf')

        ___ word __ words:
            times = self.get_times(word)
            __ l..(word) < _min_size and self.is_included(p_times, times):
                ans = word
                _min_size = l..(word)

        r.. ans

    ___ is_included(self, a_times, b_times):
        """True if A is a subset of B"""
        ___ char, times __ a_times.items():
            __ char n.. __ b_times:
                r.. False

            __ b_times[char] < times:
                r.. False

        r.. True

    ___ get_times(self, word):
        times = {}
        ord_a = ord('a')
        ord_z = ord('z')

        ___ char __ word.lower():
            __ ord_a <= ord(char) <= ord_z:
                times[char] = times.get(char, 0) + 1

        r.. times
