class Solution:
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

        for w in words:
            __ any((
                not self.is_subseq(s, w),
                len(w) < len(ans),
                len(w) == len(ans) and w >= ans,  # means w has larger lexicographical order
            )):
                continue

            ans = w

        return ans

    ___ is_subseq(self, s, t):
        """
        return True if `t` is subsequence of `s`
        """
        m, n = len(s), len(t)
        i = j = 0

        while i < m and j < n:
            __ s[i] == t[j]:
                j += 1
            i += 1

        return j == n


class Solution:
    """
    Brute Force: TLE
    """
    ___ findLongestWord(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        cands = []
        self.find_cands(s, 0, cands, [])

        ans = ''
        target = set(words)

        for w in cands:
            __ any((
                w not in target,
                len(w) < len(ans),
                len(w) == len(ans) and w >= ans,
            )):
                continue

            ans = w

        return ans

    ___ find_cands(self, s, i, cands, path):
        __ i == len(s):
            cands.append(''.join(path))
            return

        # keep s[i]
        path.append(s[i])
        self.find_cands(s, i + 1, cands, path)
        path.pop()

        # ignore s[i]
        self.find_cands(s, i + 1, cands, path)
