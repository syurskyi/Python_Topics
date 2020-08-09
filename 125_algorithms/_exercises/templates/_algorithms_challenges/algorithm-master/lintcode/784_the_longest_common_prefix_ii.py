class Solution:
    """
    @param D: the n strings
    @param target: the target string
    @return: The ans
    """
    ___ theLongestCommonPrefix(self, D, target
        ans = 0

        ___ word in D:
            i = 0
            ___ c in word:
                __ c != target[i]:
                    break
                i += 1
            __ i > ans:
                ans = i

        r_ ans
