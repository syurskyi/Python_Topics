class Solution:
    """
    1. to check the word in list is subsequence of given s
    2. ignoring if the length less than current ans
    3. ignoring if the length equal current ans but has larger lexicographical order
    """
    ___ findLongestWord(self, s, words
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        ans = ''

        ___ w in words:
            __ any((
                not self.is_subseq(s, w),
                le.(w) < le.(ans),
                le.(w) __ le.(ans) and w >= ans,  # means w has larger lexicographical order
            )):
                continue

            ans = w

        r_ ans

    ___ is_subseq(self, s, t
        """
        return True if `t` is subsequence of `s`
        """
        m, n = le.(s), le.(t)
        i = j = 0

        w___ i < m and j < n:
            __ s[i] __ t[j]:
                j += 1
            i += 1

        r_ j __ n


class Solution:
    """
    Brute Force: TLE
    """
    ___ findLongestWord(self, s, words
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        cands = []
        self.find_cands(s, 0, cands, [])

        ans = ''
        target = set(words)

        ___ w in cands:
            __ any((
                w not in target,
                le.(w) < le.(ans),
                le.(w) __ le.(ans) and w >= ans,
            )):
                continue

            ans = w

        r_ ans

    ___ find_cands(self, s, i, cands, path
        __ i __ le.(s
            cands.append(''.join(path))
            r_

        # keep s[i]
        path.append(s[i])
        self.find_cands(s, i + 1, cands, path)
        path.pop()

        # ignore s[i]
        self.find_cands(s, i + 1, cands, path)
