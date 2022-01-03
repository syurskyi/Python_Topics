c_ Solution:
    """
    1. to check the word in list is subsequence of given s
    2. ignoring if the length less than current ans
    3. ignoring if the length equal current ans but has larger lexicographical order
    """
    ___ findLongestWord(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        ans = ''

        ___ w __ words:
            __ any((
                n.. is_subseq(s, w),
                l..(w) < l..(ans),
                l..(w) __ l..(ans) a.. w >= ans,  # means w has larger lexicographical order
            )):
                continue

            ans = w

        r.. ans

    ___ is_subseq(self, s, t):
        """
        return True if `t` is subsequence of `s`
        """
        m, n = l..(s), l..(t)
        i = j = 0

        w.... i < m a.. j < n:
            __ s[i] __ t[j]:
                j += 1
            i += 1

        r.. j __ n


c_ Solution:
    """
    Brute Force: TLE
    """
    ___ findLongestWord(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        cands    # list
        find_cands(s, 0, cands, [])

        ans = ''
        target = set(words)

        ___ w __ cands:
            __ any((
                w n.. __ target,
                l..(w) < l..(ans),
                l..(w) __ l..(ans) a.. w >= ans,
            )):
                continue

            ans = w

        r.. ans

    ___ find_cands(self, s, i, cands, path):
        __ i __ l..(s):
            cands.a..(''.j..(path))
            r..

        # keep s[i]
        path.a..(s[i])
        find_cands(s, i + 1, cands, path)
        path.pop()

        # ignore s[i]
        find_cands(s, i + 1, cands, path)
