class Solution:
    ___ findSubstring(self, s, S
        """
        :type s: str
        :type S: List[str]
        :rtype: List[int]
        """
        ans = []
        __ not s or not S or le.(s) < le.(S) * le.(S[0]
            r_ ans

        n, m, k = le.(s), le.(S), le.(S[0])
        F = {}
        ___ c in S:
            F[c] = F.get(c, 0) + 1

        ___ start in range(k
            _F = {}
            cnt = 0
            left = start

            ___ right in range(start, n - k + 1, k
                sr = s[right:right + k]
                __ sr not in F:
                    _F = {}
                    cnt = 0
                    left = right + k
                    continue

                _F[sr] = _F.get(sr, 0) + 1
                __ _F[sr] <= F[sr]:
                    cnt += 1
                w___ _F[sr] > F[sr]:
                    sl = s[left:left + k]
                    __ _F[sl] __ F[sl]:
                        cnt -= 1
                    _F[sl] -= 1
                    left += k

                __ cnt __ m:
                    ans.append(left)
                    sl = s[left:left + k]
                    cnt -= 1
                    _F[sl] -= 1
                    left += k

        r_ ans
