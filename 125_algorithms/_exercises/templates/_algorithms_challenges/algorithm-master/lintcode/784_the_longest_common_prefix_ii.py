class Solution:
    """
    @param D: the n strings
    @param target: the target string
    @return: The ans
    """
    ___ theLongestCommonPrefix(self, D, target
        ans = 0

        for word in D:
            i = 0
            for c in word:
                __ c != target[i]:
                    break
                i += 1
            __ i > ans:
                ans = i

        r_ ans
