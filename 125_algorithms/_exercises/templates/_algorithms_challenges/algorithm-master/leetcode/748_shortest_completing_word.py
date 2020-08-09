class Solution:
    ___ shortestCompletingWord(self, P, words
        """
        :type P: str
        :type words: List[str]
        :rtype: str
        """

        ans = ''
        __ not P or not words:
            r_ ans

        p_times = self.get_times(P)
        _min_size = float('inf')

        ___ word in words:
            times = self.get_times(word)
            __ le.(word) < _min_size and self.is_included(p_times, times
                ans = word
                _min_size = le.(word)

        r_ ans

    ___ is_included(self, a_times, b_times
        """True if A is a subset of B"""
        ___ char, times in a_times.items(
            __ char not in b_times:
                r_ False

            __ b_times[char] < times:
                r_ False

        r_ True

    ___ get_times(self, word
        times = {}
        ord_a = ord('a')
        ord_z = ord('z')

        ___ char in word.lower(
            __ ord_a <= ord(char) <= ord_z:
                times[char] = times.get(char, 0) + 1

        r_ times
